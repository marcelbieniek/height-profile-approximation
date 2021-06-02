from sampler import *


def interpolate(samples, distance):
    length = len(samples["distance"])
    elevation = 0

    for i in range(length):
        phi = 1

        x_i = samples["distance"][i]
        for j in range(length):
            if i != j:
                x_j = samples["distance"][j]

                phi *= (distance - x_j) / (x_i - x_j)

        elevation += phi * samples["elevation"][i]

    return elevation


def lagrange_interpolation(data, interval, randomised=False, force_edges=False):
    samples = generate_samples(data, interval, randomised, force_edges)

    elevation = []
    for i in range(len(data["distance"])):
        elevation.append(interpolate(samples, data["distance"][i]))

    return samples, {"distance": data["distance"], "elevation": elevation}
