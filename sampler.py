from numpy import random
import math


def get_new_index(indexes, size):
    while True:
        index = random.randint(size)
        if index not in indexes:
            return index


def generate_samples(data, interval, randomised=False, force_edges=False):
    distance = []
    elevation = []

    if not randomised:
        distance = data["distance"][::interval]
        elevation = data["elevation"][::interval]

        if force_edges and data["distance"][-1] not in distance:
            distance.append(data["distance"][-1])
            elevation.append(data["elevation"][-1])
    else:
        data_length = len(data["distance"])
        num_of_samples = math.ceil(data_length / interval)

        samples_indexes = []
        if force_edges:
            samples_indexes.append(0)
            samples_indexes.append(data_length - 1)
            num_of_samples -= 2

        for i in range(num_of_samples):
            samples_indexes.append(get_new_index(samples_indexes, data_length - 1))

        samples_indexes.sort()

        for i in range(len(samples_indexes)):
            distance.append(data["distance"][samples_indexes[i]])
            elevation.append(data["elevation"][samples_indexes[i]])

    return {"distance": distance, "elevation": elevation}
