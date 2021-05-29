from file_loader import *
from plotter import *

DATA_PATH = "data/"
FILE_NAME = "100.csv"

if __name__ == "__main__":
    data = load_file(DATA_PATH + FILE_NAME)

    plot_profile(data, FILE_NAME)
