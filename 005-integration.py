import time
import functools
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

def printTime (func) :
    @functools.wraps(func)
    def wrapper (*args, **kwargs) :
        tic = time.perf_counter()
        result = func(*args, **kwargs)
        toc = time.perf_counter()
        print(f"{func.__name__} ran for {(toc - tic) * 1000:.2f} ms")
        return result
    return wrapper

def integrand_func (x) : return np.exp( np.sin(x) )
integrand_lambda = lambda x :   np.exp( np.sin(x) )

a = 0
b = 150

@printTime
def intFunc () :
    return integrate.quad( integrand_func, a, b )

@printTime
def intLambda () :
    return integrate.quad( integrand_lambda, a, b )

@printTime
def intSimpson () :
    return integrate.simps(Y, dx = (b - a) / N)

@printTime
def intRomb () :
    return integrate.romb(Y, dx = (b - a) / N)




print( intFunc   () )
print( intLambda () )
print()

k = 16
tic = time.perf_counter()
N = 2**k + 1
X = np.linspace(a, b, N)
Y = integrand_lambda(X)
toc = time.perf_counter()
print(f"preparation ran for {(toc - tic) * 1000:.2f} ms")
print()

print( intSimpson() )
print( intRomb   () )

plt.plot(X, Y)
plt.show()