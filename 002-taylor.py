#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10,7)

def makeSeries (N) :
    def outer(expr) :
        def wrapper(*args, **kwargs) :
            result = 0
            for n in range(N) :
                result += expr(n, *args, **kwargs)
            return result
        return wrapper
    return outer


N = 10
approximations = []
for n in range(1, N) :
    @makeSeries(n)
    def sine(n, x) :
        return ((-1)**n / np.math.factorial(2*n + 1)) * x**(2*n + 1)
    
    approximations.append(sine)

X = np.linspace(0, 2*np.pi, 314)
for n, sin in enumerate(approximations) :
    plt.plot(X, sin(X), label=f"degree {n+1}", color=f"#0088{n}{n}ff")

plt.ylim(-1.5, +1.5)
plt.plot(X, np.sin(X), label="numpy sin", color='r')
plt.legend(loc="lower left")

plt.show()