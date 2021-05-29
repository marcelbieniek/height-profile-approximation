import matplotlib.pyplot as plt


def plot_profile(data, title):
    plt.plot(data["distance"], data["elevation"])
    plt.title(title)
    plt.xlabel("Distance (m)")
    plt.ylabel("Elevation (m)")
    plt.show()
