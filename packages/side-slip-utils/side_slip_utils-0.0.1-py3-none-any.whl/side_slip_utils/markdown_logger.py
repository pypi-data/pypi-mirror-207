import pandas as pd


def write_model(model, writer, topic="Model_Params"):
    model_df = []
    for layer in model.__str__().splitlines()[1:-1]:
        try:
            model_df.append(
                {
                    model.__str__().splitlines()[0].split("(")[0]: layer.split(":")[0],
                    "Layer Structure": layer.split(":")[1],
                }
            )
        except:
            pass
    model_mkd = pd.DataFrame(model_df).to_markdown(index=False)
    model_mkd = "\n".join(l.strip() for l in model_mkd.splitlines())
    writer.add_text(topic, model_mkd)


def write_optimizer(optimizer, writer, topic="Model_Params"):
    optimizer_df = []
    for setting in optimizer.__str__().splitlines()[2:-1]:
        optimizer_df.append(
            {
                optimizer.__str__()
                .splitlines()[0]
                .split("(")[0]: setting.split(":")[0],
                "Value": setting.split(":")[1],
            }
        )
    optimizer_mkd = pd.DataFrame(optimizer_df).to_markdown(index=False)
    optimizer_mkd = "\n".join(l.strip() for l in optimizer_mkd.splitlines())
    writer.add_text(topic, optimizer_mkd)
