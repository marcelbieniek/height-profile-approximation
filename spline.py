from sampler import generate_samples
from LU import solve


def get_lu_data(samples):
    n = len(samples["distance"])
    x = []
    y = []
    for i in range(n):
        x.append(samples["distance"][i])
        y.append(samples["elevation"][i])

    num_of_intervals = 4 * (n - 1)
    A = [[0 for _ in range(num_of_intervals)] for _ in range(num_of_intervals)]
    b = [0 for _ in range(num_of_intervals)]

    # S0(x0) = f(x0)
    A[0][0] = 1
    b[0] = y[0]
    h = x[1] - x[0]

    # S0(x1) = f(x1)
    A[1][0] = 1
    A[1][1] = h
    A[1][2] = h ** 2
    A[1][3] = h ** 3
    b[1] = y[1]

    # S0"(x0) = 0
    A[2][2] = 1
    b[2] = 0

    # Sn-1"(xn) = 0
    h = x[-1] - x[-2]
    # h = x[n - 1] - x[n - 2]
    A[3][4 * (n - 2) + 2] = 2
    A[3][4 * (n - 2) + 3] = 6 * h
    b[3] = 0

    for i in range(1, n - 1):
        h = x[i] - x[i - 1]

        # Si(xi) = f(xi)
        A[4 * i][4 * i] = 1
        b[4 * i] = y[i]

        # Si(xi+1) = f(x+1)
        A[4 * i + 1][4 * i] = 1
        A[4 * i + 1][4 * i + 1] = h
        A[4 * i + 1][4 * i + 2] = h ** 2
        A[4 * i + 1][4 * i + 3] = h ** 3
        b[4 * i + 1] = y[i + 1]

        # Si-1'(xi) = Si'(xi)
        A[4 * i + 2][4 * (i - 1) + 1] = 1
        A[4 * i + 2][4 * (i - 1) + 2] = 2 * h
        A[4 * i + 2][4 * (i - 1) + 3] = 3 * (h ** 2)
        A[4 * i + 2][4 * i + 1] = -1
        b[4 * i + 2] = 0

        # Si-1"(xi) = Si"(xi)
        A[4 * i + 3][4 * (i - 1) + 2] = 2
        A[4 * i + 3][4 * (i - 1) + 3] = 6 * h
        A[4 * i + 3][4 * i + 2] = -2
        b[4 * i + 3] = 0

    return A, b


def interpolate(samples, distance, x):
    length = len(samples["distance"])

    for i in range(1, length):
        if samples["distance"][i - 1] <= distance <= samples["distance"][i]:
            a = x[4 * i - 4]
            b = x[4 * i - 3]
            c = x[4 * i - 2]
            d = x[4 * i - 1]
            h = distance - samples["distance"][i - 1]

            return a + b * h + c * h ** 2 + d * h ** 3


def spline_interpolation(data, interval, randomised=False, force_edges=False):
    samples = generate_samples(data, interval, randomised, force_edges)

    A, b = get_lu_data(samples)
    x = solve(A, b)

    elevation = []
    for i in range(len(data["distance"])):
        elevation.append(interpolate(samples, data["distance"][i], x))

    return samples, {"distance": data["distance"], "elevation": elevation}
