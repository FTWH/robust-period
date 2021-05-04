import numpy as np
import matplotlib.pyplot as plt


def huber_acf(periodogram):
    N_prime = len(periodogram)
    N = N_prime // 2
    K = np.arange(N)

    cond_1 = periodogram[range(N)]
    cond_2 = (periodogram[2 * K] - periodogram[2 * K + 1]).sum() ** 2 / N_prime
    cond_3 = [periodogram[N_prime - k] for k in range(N + 1, N_prime)]

    P_bar = np.hstack([cond_1, cond_2, cond_3])
    P = np.fft.ifft(P_bar)

    denom = (N - np.arange(0, N)) * P[0]
    res = P[:N] / denom

    return res


if __name__ == '__main__':
    periodograms = np.loadtxt('periodograms.csv', delimiter=',')

    per = periodograms[0]

    N = len(per)
    k = np.argmax(per)
    print(0.5 * ((N/(k+1)) + (N/k)) - 1, 0.5 * ((N/k) + (N/(k-1))) + 1)
    # print(N/k)

    res = huber_acf(per)

    from scipy.signal import find_peaks
    peaks, _ = find_peaks(res)
    distances = np.diff(peaks)
    final_period = np.median(distances)
    print(final_period)

    plt.plot(res[:800])
    plt.show()
