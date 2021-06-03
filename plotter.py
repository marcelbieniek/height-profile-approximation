import matplotlib.pyplot as plt


def plot_profile(data, title, dots=False):
    plt.plot(data["distance"], data["elevation"])
    if dots:
        plt.plot(data["distance"], data["elevation"], 'o')
    plt.title(title)
    plt.xlabel("Distance (m)")
    plt.ylabel("Elevation (m)")
    plt.show()


def plot_with_interpolation(data, samples, interpolated_data, method, file_name, dots=False):
    plt.plot(data["distance"], data["elevation"], label='original')
    plt.plot(interpolated_data["distance"], interpolated_data["elevation"], label='interpolated')
    if dots:
        plt.plot(samples["distance"], samples["elevation"], 'o', label='samples')
    plt.title(method + ": " + file_name + " interpolated with " + str(len(samples["distance"])) + " samples")
    plt.xlabel("Distance (m)")
    plt.ylabel("Elevation (m)")
    plt.legend()
    plt.show()


def plot_both_with_interpolation(data, samples_1, interpolated_data_1, samples_2, interpolated_data_2, file_name, dots=False):
    fig, axs = plt.subplots(1, 2)
    fig.suptitle(f"{file_name}")
    fig.set_figwidth(12)

    axs[0].plot(data["distance"], data["elevation"], label='original')
    axs[0].plot(interpolated_data_1["distance"], interpolated_data_1["elevation"], label='interpolated')
    if dots:
        axs[0].plot(samples_1["distance"], samples_1["elevation"], 'o', label='samples')
    axs[0].set_title(f"Lagrange, {len(samples_1['distance'])} samples")

    axs[1].plot(data["distance"], data["elevation"], label='original')
    axs[1].plot(interpolated_data_2["distance"], interpolated_data_2["elevation"], label='interpolated')
    if dots:
        axs[1].plot(samples_2["distance"], samples_2["elevation"], 'o', label='samples')
    axs[1].set_title(f"Spline, {len(samples_2['distance'])} samples")

    for ax in axs.flat:
        ax.set(xlabel="Distance (m)", ylabel="Elevation (m)")

    plt.legend()
    file = file_name.split(".")
    plt.savefig(f"plots/{file[0]} - {len(samples_1['distance'])} samples.png")
    plt.show()


def plot_samples(samples):
    plt.plot(samples["distance"], samples["elevation"], 'o', label='samples')
    plt.xlabel("Distance (m)")
    plt.ylabel("Elevation (m)")
    plt.legend()
    plt.show()
