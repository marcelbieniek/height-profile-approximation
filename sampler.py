from numpy import random
import math


def generate_samples(data, interval, randomised=False):
    distance = []
    elevation = []

    if not randomised:
        distance = data["distance"][::interval]
        elevation = data["elevation"][::interval]
    else:
        num_of_samples = math.ceil(len(data["distance"]) / interval)

        samples_indexes = []
        for i in range(num_of_samples):
            while True:
                index = random.randint(len(data["distance"]) - 1)
                if index not in samples_indexes:
                    break

            samples_indexes.append(index)
        samples_indexes.sort()

        for i in range(num_of_samples):
            distance.append(data["distance"][samples_indexes[i]])
            elevation.append(data["elevation"][samples_indexes[i]])

    return {"distance": distance, "elevation": elevation}
