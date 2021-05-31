from numpy import random
import math


def get_new_index(indexes, size):
    while True:
        index = random.randint(size)
        if index not in indexes:
            return index


def generate_samples(data, interval, randomised=False, force_last=False):
    distance = []
    elevation = []

    if not randomised:
        distance = data["distance"][::interval]
        elevation = data["elevation"][::interval]

        if force_last and data["distance"][-1] not in distance:
            distance.append(data["distance"][-1])
            elevation.append(data["elevation"][-1])
    else:
        num_of_samples = math.ceil(len(data["distance"]) / interval)

        samples_indexes = []
        for i in range(num_of_samples):
            samples_indexes.append(get_new_index(samples_indexes, len(data["distance"]) - 1))

        samples_indexes.sort()

        for i in range(num_of_samples):
            distance.append(data["distance"][samples_indexes[i]])
            elevation.append(data["elevation"][samples_indexes[i]])

        if force_last:
            distance.append(data["distance"][-1])
            elevation.append(data["elevation"][-1])

    return {"distance": distance, "elevation": elevation}
