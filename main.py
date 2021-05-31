from file_loader import *
from plotter import *
from lagrange import *

DATA_PATH = "data/"
FILE_NAME = "ostrowa.txt"

if __name__ == "__main__":
    data = load_file(DATA_PATH + FILE_NAME)
    plot_profile(data, FILE_NAME)

    samples, interpolated_data = lagrange_interpolation(data, 10, randomised=False)
    plot_with_interpolation(data, samples, interpolated_data, FILE_NAME + " interpolated", dots=True)
