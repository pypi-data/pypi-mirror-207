import torch
from pathlib import Path
import pandas as pd
import numpy as np
from torch.utils.data import ConcatDataset, Dataset, DataLoader, random_split
import pkg_resources
import glob
import matplotlib.pyplot as plt

file_path = {
    "2013_Targa_Sixty_Six": "data/processed/2013_Targa_Sixty_Six",
    "2014_Targa_Sixty_Six": "data/processed/2014_Targa_Sixty_Six",
    "2013_Laguna_Seca": "data/processed/2013_Laguna_Seca",
}

columns_to_standardize = [
    "engineSpeed",
    "handwheelAngle",
    "throttle",
    "brake",
    "axCG",
    "ayCG",
    "yawRate",
    "chassisAccelFL",
    "chassisAccelFR",
    "chassisAccelRL",
    "chassisAccelRR",
]


class CarDataset(Dataset):
    def __init__(
        self, df, target, seq_length, dtype=torch.float32, loop_predictions=False
    ):
        self.data = df.copy(deep=True)
        self.seq_length = seq_length
        self.y = torch.tensor(self.data[target].to_numpy(), dtype=dtype)
        self.X = torch.tensor(
            self.data.drop(
                ["sideSlip", "vxCG", "vyCG", "time", "longitude", "latitude"], axis=1
            ).to_numpy(),
            dtype=dtype,
        )
        self.loop_predictions = loop_predictions

    def __getitem__(self, index):
        x = self.X[index : index + self.seq_length]
        y = self.y[index + self.seq_length - 1]  # -1 important to avoid forecasting!
        if self.loop_predictions:
            y_t = self.y[index + self.seq_length - 2]  # -2 for the "last prediction"
            return x, y, y_t
        return x, y

    def __len__(self):
        return len(self.data) - self.seq_length


def create_train_dataset(
    folder,
    seq_length=20,
    val_split=False,
    num_csv=np.inf,
    target="sideSlip",
    standardize=False,
    cols_to_standardize=columns_to_standardize,
    threshold=None,
    bound=None,
    loop_prediction=False,
):
    path = pkg_resources.resource_filename(__name__, file_path[folder])

    returns = []

    # Exceptions
    if val_split and num_csv < 2:
        raise Exception(
            "num_csv has to be atleast 2 if validation_split is True. Otherwise it cannot perfrom a split!"
        )

    # Collect all DFs in a list
    dflist = []
    file_ls = []
    for i, fname in enumerate(sorted(glob.glob(path + "/*.csv"))):
        if i >= num_csv:
            break
        elif i == 0 and val_split:
            valdf = pd.read_csv(fname, sep=",")
            file_ls.append(fname.split("/")[-1])
            continue

        dflist.append(pd.read_csv(fname, sep=","))
        file_ls.append(fname.split("/")[-1])

    # Apply threshold
    if threshold is not None:
        if bound is None:
            raise Exception("bound has to be provided if threshold is not None!")

        new_dflist = []
        for df in dflist:
            df_mask = df["vxCG"].rolling(bound, center=True).max() > threshold

            cont_df = pd.DataFrame([])
            detected = False
            start_index = 0
            stop_index = 0

            for index, bool in enumerate(df_mask):
                if bool and detected == False:
                    start_index = index
                    detected = True

                elif bool == False and detected == True:
                    stop_index = index

                    cont_df = df.iloc[start_index:stop_index]
                    new_dflist.append(cont_df)
                    cont_df = pd.DataFrame([])

                    detected = False

        dflist = new_dflist

    # Standardize
    if standardize:
        concatdf = pd.concat(dflist)
        mean = concatdf[cols_to_standardize].mean()
        std = concatdf[cols_to_standardize].std()

        for i, df in enumerate(dflist):
            dflist[i][cols_to_standardize] = (df[cols_to_standardize] - mean) / std

        if val_split:
            valdf[cols_to_standardize] = (valdf[cols_to_standardize] - mean) / std

    else:
        mean = None
        std = None

    returns.append(std)
    returns.append(mean)
    returns.append(file_ls)

    # Create Train datasets
    datasets = []
    for i, data in enumerate(dflist):
        datasets.append(
            CarDataset(
                df=data,
                target=target,
                seq_length=seq_length,
                loop_predictions=loop_prediction,
            )
        )
    datasets = ConcatDataset(datasets)

    # Create Val datasets
    if val_split:
        validationset = CarDataset(df=valdf, target=target, seq_length=seq_length)
    else:
        validationset = None

    returns.append(validationset)
    returns.append(datasets)
    returns.reverse()
    # Return
    return returns


def create_test_dataset(
    folder,
    seq_length=20,
    val_split=False,
    num_csv=np.inf,
    target="sideSlip",
    mean=None,
    std=None,
    cols_to_standardize=columns_to_standardize,
):
    path = pkg_resources.resource_filename(__name__, file_path[folder])

    returns = []

    # Exceptions
    if (
        mean is not None and std is None or mean is None and std is not None
    ):  # beautiful :D
        raise Exception("mean and std have both to be provided!")

    if val_split and num_csv < 2:
        raise Exception(
            "num_csv has to be atleast 2 if validation_split is True. Otherwise it cannot perfrom a split!"
        )

    # Collect all DFs in a list
    dflist = []
    file_ls = []

    for i, fname in enumerate(sorted(glob.glob(path + "/*.csv"))):
        if i >= num_csv:
            break
        dflist.append(pd.read_csv(fname, sep=","))
        file_ls.append(fname.split("/")[-1])

    # Standardize
    if mean is not None:
        for i, data in enumerate(dflist):
            dflist[i][cols_to_standardize] = (data[cols_to_standardize] - mean) / std

    returns.append(file_ls)

    # Create datasets
    datasets = []
    for i, data in enumerate(dflist):
        if i == 0 and val_split:
            validationset = CarDataset(df=data, target=target, seq_length=seq_length)
            returns.append(validationset)
        else:
            datasets.append(CarDataset(df=data, target=target, seq_length=seq_length))

    returns.append(datasets)
    returns.reverse()
    return returns


def create_level_dataset(
    level=1,
    target="sideSlip",
    inverse=False,
    seq_length=20,
    batchsize=32,
    standardize=False,
    verbose=False,
    threshold=None,
    bound=200,
    loop_prediction=False,
):
    test_dataloader = {}
    if level == 0:
        train_ds, val_ds, train_ls, mean, std = create_train_dataset(
            folder="2013_Laguna_Seca",
            target=target,
            seq_length=seq_length,
            val_split=True,
            standardize=standardize,
            threshold=threshold,
            bound=bound,
            loop_prediction=loop_prediction,
        )

        if loop_prediction:
            val_ds = torch.utils.data.Subset(val_ds, range(0, int(len(val_ds) / 2)))
            test_ds = torch.utils.data.Subset(
                val_ds, range(int(len(val_ds) / 2), len(val_ds))
            )
        else:
            val_ds, test_ds = random_split(val_ds, [0.5, 0.5])
        test_dataloader["Level_0_Test_Split"] = DataLoader(
            test_ds, batch_size=1, shuffle=False
        )
        test_list = train_ls
    elif level == 1:
        paths = ["2013_Laguna_Seca", "2013_Targa_Sixty_Six"]
    elif level == 2:
        paths = ["2013_Targa_Sixty_Six", "2014_Targa_Sixty_Six"]
    elif level == 3:
        paths = ["2013_Laguna_Seca", "2014_Targa_Sixty_Six"]
    else:
        raise Exception(
            f"Level has to be between 0 and 3! It has level {level} with type {type(level)}"
        )

    if level > 0:
        if inverse:
            paths.reverse()

        train_ds, val_ds, train_ls, mean, std = create_train_dataset(
            folder=paths[0],
            target=target,
            val_split=True,
            seq_length=seq_length,
            standardize=standardize,
            threshold=threshold,
            bound=bound,
            loop_prediction=loop_prediction,
        )

        test_ds, test_list = create_test_dataset(
            folder=paths[1], target=target, seq_length=seq_length, mean=mean, std=std
        )

        for i, dataset in enumerate(test_ds):
            test_dataloader[test_list[i]] = DataLoader(
                dataset, batch_size=1, shuffle=False
            )

    train_dataloader = DataLoader(train_ds, batch_size=batchsize, shuffle=True)

    if loop_prediction:
        validation_dataloader = DataLoader(val_ds, batch_size=1, shuffle=False)
    else:
        validation_dataloader = DataLoader(val_ds, batch_size=batchsize, shuffle=True)

    if verbose:
        print("Length of Train Data      ", len(train_dataloader) * batchsize)
        print("Length of Validation Data ", len(validation_dataloader) * batchsize)
        print(
            "Length of Test Data       ",
            sum([len(dl) for dl in list(test_dataloader.values())]),
        )
        print(
            "Train\Test Ratio          ",
            round(
                sum([len(ds) for ds in test_ds])
                / (len(train_ds) + sum([len(ds) for ds in test_ds])),
                2,
            ),
        )
        print("Size of Feature Space     ", len(train_ds[0][0][0]))
    return (
        train_dataloader,
        validation_dataloader,
        test_dataloader,
        train_ls,
        test_list,
    )
