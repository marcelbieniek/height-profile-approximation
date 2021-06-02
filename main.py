from file_loader import *
from plotter import *
from lagrange import lagrange_interpolation
from spline import spline_interpolation

DATA_PATH = "data/"
FILE_NAME = "ostrowa.txt"
INTERVAL = 65

if __name__ == "__main__":
    data = load_file(DATA_PATH + FILE_NAME)
    plot_profile(data, FILE_NAME)

    samples, interpolated_data = lagrange_interpolation(data, INTERVAL, randomised=False, force_edges=True)
    plot_with_interpolation(data, samples, interpolated_data, "Lagrange", FILE_NAME, dots=True)

    samples, interpolated_data = spline_interpolation(data, INTERVAL, randomised=False, force_edges=True)
    plot_with_interpolation(data, samples, interpolated_data, "Spline", FILE_NAME, dots=True)
