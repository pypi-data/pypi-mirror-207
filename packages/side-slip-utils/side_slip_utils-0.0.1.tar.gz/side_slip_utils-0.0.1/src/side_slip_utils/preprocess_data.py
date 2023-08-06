import glob
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

path = f"{os.path.abspath(os.getcwd())}/data/raw/"
print(path)

target_folder = [
    name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))
]
print(target_folder)

for folder in target_folder:
    subfolder = f"{path}{folder}/*.csv"

    for fname in glob.glob(subfolder):
        print(fname)

        file_name = fname.split("/")[-1].split(".")[0]
        # Maybe For Windows!
        # file_name = fname.split("\\")[-1].split(".")[0]

        df = pd.read_csv(
            fname, skiprows=10, header=[0, 1], encoding="unicode_escape", sep=","
        )
        df.columns = df.columns.droplevel(-1)
        # TODO: Remove speeds below 1 kmh at the start and end of each df
        df = df[
            [
                "sideSlip",
                "vxCG",
                "vyCG",
                "time",
                "horizontalSpeed",
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
                "longitude",
                "latitude"
            ]
        ]  # .astype("float32")
        df = df.round(
            {
                "time": 3
            }
        )

        # downsample to 20 hz -> 1/20 = 0.05s
        df.index = pd.to_datetime(df["time"], unit = 's')
        df = df.resample("0.05S").first()
        df.reset_index(inplace=True, drop=True)
        

        df_cache = df[["sideSlip", "vxCG","vyCG", "time", "longitude", "latitude"]]
    	
        df.drop(["sideSlip", "vxCG","vyCG", "time", "longitude", "latitude"], axis= 1, inplace = True)

        """
        # scale features to have a mean of 0 and a std of 1
        scaler = StandardScaler()
        df_cache = df[["sideSlip", "vxCG","vyCG", "time", "longitude", "latitude"]]
        df.drop(["sideSlip", "vxCG","vyCG", "time", "longitude", "latitude"], axis= 1, inplace = True)
        cols = df.columns
        df_scaled = scaler.fit_transform(df)
        df = pd.DataFrame(df_scaled,columns=cols)
        """

        # round all but the targets, location data and time
        df = df.round(2)
        df = pd.concat([df_cache,df], axis = 1)

        if df.isnull().sum().sum() > 0:
            
            print("Attention, None Values found in:")
            print(file_name)
            print(df.isnull().sum())

        df.to_csv(
            f"{os.path.abspath(os.getcwd())}/data/processed/{file_name}_processed.csv",
            index=False,
        )
