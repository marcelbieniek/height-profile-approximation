from file_loader import *
from plotter import *
from lagrange import lagrange_interpolation
from spline import spline_interpolation


DATA_PATH = "data/"
FILE_NAMES = ["SpacerniakGdansk.csv",
              "stale.txt",
              "100.csv",
              "Unsyncable_ride.csv",
              "ostrowa.txt",
              "molo_brzezno_sopot.csv",
              "chelm.txt",
              "genoa_rapallo.txt",
              "GlebiaChallengera.csv",
              "Hel_yeah.csv",
              "in_mountain.data",
              "MountEverest.csv",
              "Obiadek.csv",
              "przyk3.txt",
              "Redlujjj.csv",
              "rozne_wniesienia.txt",
              "tczew_starogard.txt",
              "ulm_lugano.txt",
              "WielkiKanionKolorado.csv"]


if __name__ == "__main__":

    INTERVAL = [90, 60, 35, 20, 10]  # distance between each sample
    first_x_files = 3  # how many files to use

    for i in range(first_x_files):
        data = load_file(DATA_PATH + FILE_NAMES[i])
        # plot_profile(data, FILE_NAMES[i])
        for j in range(len(INTERVAL)):

            samples_1, interpolated_data_1 = lagrange_interpolation(data, INTERVAL[j], randomised=False, force_edges=True)
            # plot_with_interpolation(data, samples_1, interpolated_data_1, "Lagrange", FILE_NAMES[i], dots=True)

            samples_2, interpolated_data_2 = spline_interpolation(data, INTERVAL[j], randomised=False, force_edges=True)
            # plot_with_interpolation(data, samples_2, interpolated_data_2, "Spline", FILE_NAMES[i], dots=True)

            plot_both_with_interpolation(data, samples_1, interpolated_data_1, samples_2, interpolated_data_2, FILE_NAMES[i], dots=True)
