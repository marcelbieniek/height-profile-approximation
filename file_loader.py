import pandas as pd

def load_file(path):
    data = pd.read_csv(path)

    return data