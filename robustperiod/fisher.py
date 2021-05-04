import numpy as np


def fisher(periodogram):
    N_prime = len(periodogram)
    N = N_prime // 2
    g = np.max(periodogram / np.sum(periodogram))

    upper = int(np.floor(1/g))

    fac = np.math.factorial

    tot = 0
    for k in range(1, upper + 1):
        tot += ((((-1) ** (k-1)) * fac(N)) /
                (fac(k) * fac(N-k))) * ((1-k*g)**(N-1))
    p = 1 - tot

    return p


if __name__ == '__main__':
    periodograms = np.loadtxt('periodograms.csv', delimiter=',')

    fisher(periodograms[0])
