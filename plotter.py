import matplotlib.pyplot as plt


def plot_profile(data, title, dots=False):
    plt.plot(data["distance"], data["elevation"])
    if dots:
        plt.plot(data["distance"], data["elevation"], 'o')
    plt.title(title)
    plt.xlabel("Distance (m)")
    plt.ylabel("Elevation (m)")
    plt.show()


def plot_with_interpolation(data, samples, interpolated_data, file_name, num_of_samples, dots=False):
    plt.plot(data["distance"], data["elevation"], label='original')
    plt.plot(interpolated_data["distance"], interpolated_data["elevation"], label='interpolated')
    if dots:
        plt.plot(samples["distance"], samples["elevation"], 'o', label='samples')
    plt.title(file_name + " interpolated with " + str(num_of_samples) + " samples")
    plt.xlabel("Distance (m)")
    plt.ylabel("Elevation (m)")
    plt.legend()
    plt.show()
