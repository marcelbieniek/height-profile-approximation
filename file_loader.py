import pandas as pd


def load_file(path):
    data = pd.read_csv(path)
    return {"distance": data["Distance(m)"].tolist(), "elevation": data["Elevation(m)"].tolist()}
