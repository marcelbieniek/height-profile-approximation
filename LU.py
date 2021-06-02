def eye(n):
    A = []

    for i in range(n):
        A.append([0 for _ in range(n)])
        A[i][i] = 1

    return A


def copy_matrix(A):
    B = []
    n = len(A)

    for i in range(n):
        B.append([0 for _ in range(n)])
        for j in range(n):
            B[i][j] = A[i][j]

    return B


def do_pivot(L, P, U, k):
    pivot = abs(U[k][k])
    ind = k

    for i in range(k + 1, len(U)):
        if abs(U[i][k]) > pivot:
            pivot = abs(U[i][k])
            ind = i

    if U[ind][k] == 0:
        print("Matrix is singular")
        return

    # interchange rows
    if ind != k:
        for i in range(len(U)):
            if i >= k:
                tmp = U[k][i]
                U[k][i] = U[ind][i]
                U[ind][i] = tmp
            else:
                tmp = L[k][i]
                L[k][i] = L[ind][i]
                L[ind][i] = tmp

            tmp = P[k][i]
            P[k][i] = P[ind][i]
            P[ind][i] = tmp


def decompose(A):
    n = len(A)
    L = eye(n)
    P = eye(n)
    U = copy_matrix(A)

    for k in range(n - 1):

        do_pivot(L, P, U, k)

        for j in range(k + 1, n):
            L[j][k] = U[j][k] / U[k][k]

            for i in range(k, n):
                U[j][i] = U[j][i] - L[j][k] * U[k][i]

    return L, U


def forward_substitution(b, L):
    n = len(L)
    x = [0 for _ in range(n)]

    for i in range(n):
        nominator = b[i]

        for j in range(i):
            nominator -= L[i][j] * x[j]

        x[i] = nominator / L[i][i]

    return x


def backward_substitution(b, U):
    n = len(U)
    x = [0 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        nominator = b[i]

        for j in range(i + 1, n):
            nominator -= U[i][j] * x[j]

        x[i] = nominator / U[i][i]

    return x


def solve(A, b):
    L, U = decompose(A)

    y = forward_substitution(b, L)

    x = backward_substitution(y, U)

    return x
