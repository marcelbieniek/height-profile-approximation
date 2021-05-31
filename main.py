from file_loader import *
from plotter import *
from lagrange import *

DATA_PATH = "data/"
FILE_NAME = "ostrowa.txt"
INTERVAL = 50

if __name__ == "__main__":
    data = load_file(DATA_PATH + FILE_NAME)
    # plot_profile(data, FILE_NAME)

    num_of_samples = math.ceil(len(data["distance"]) / INTERVAL)
    samples, interpolated_data = lagrange_interpolation(data, INTERVAL, randomised=False, force_last=False)
    plot_with_interpolation(data, samples, interpolated_data, FILE_NAME, num_of_samples, dots=True)
