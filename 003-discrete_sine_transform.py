import scipy
import numpy as np
import matplotlib.pyplot as plt

N = 6280
P = 4
X = np.linspace(0, P * np.pi, N)
Y = np.sin(np.pi * X) + .3 * np.sin(5 * np.pi * X)

A = scipy.fft.dst(Y, norm="ortho")
W = [k / (P * np.pi) for k in range(len(A))]

spectrumLimit = 100

fig = plt.figure( figsize=(5, 10) )
drw = fig.add_subplot(211)
drw.set_xlabel("time t")
drw.set_ylabel("signal intensity")
drw.plot(X, Y)

drw = fig.add_subplot(212)
drw.set_xlabel("angular frequency $\omega$")
drw.set_ylabel("signal amplitude")
drw.plot(W[:spectrumLimit], A[:spectrumLimit])

plt.show()
