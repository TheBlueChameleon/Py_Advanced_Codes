import time
import functools
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

# =========================================================================== #

def appendTime (func) :
    @functools.wraps(func)
    def wrapper (*args, **kwargs) :
        tic = time.perf_counter()
        result = func(*args, **kwargs)
        toc = time.perf_counter()
        return result, toc - tic
    return wrapper

# =========================================================================== #

@appendTime
def intSimp (Y, dx) :
    return integrate.simps(Y, dx=dx)

@appendTime
def intRomb (Y, dx) :
    return integrate.romb(Y, dx=dx)

@appendTime
def intTrap (Y, dx) :
    return integrate.trapz(Y, dx=dx)

@appendTime
def intQuad (f, a, b) :
  return integrate.quad( f, a, b, )

# =========================================================================== #

a = 0
b = 150

integrand_lambda = lambda x : np.exp( np.sin(x) ) + np.exp( np.cos(x) )
# try this as a test integrand
# lambda x : 1 if type(x) == float else np.ones(len(x)) # 

((exact, accuracy), tquad) = intQuad( integrand_lambda, a, b )

K = range(1, 27)
times_S = []
times_R = []
times_T = []
resdevS = []
resdevR = []
resdevT = []

for k in K :
    tic = time.perf_counter()
    N = 2**k + 1
    X = np.linspace(a, b, N)
    Y = integrand_lambda(X)
    toc = time.perf_counter()
    
    res_romb = intRomb(Y, (b - a) / N)
    res_simp = intSimp(Y, (b - a) / N)
    res_trap = intTrap(Y, (b - a) / N)
    
    times_S.append( (toc - tic, res_simp[-1], toc - tic + res_simp[-1]) )
    times_R.append( (toc - tic, res_romb[-1], toc - tic + res_romb[-1]) )
    times_T.append( (toc - tic, res_trap[-1], toc - tic + res_trap[-1]) )
    
    resdevS.append( (res_simp[0], abs(res_simp[0] - exact)) )
    resdevR.append( (res_romb[0], abs(res_romb[0] - exact)) )
    resdevT.append( (res_trap[0], abs(res_trap[0] - exact)) )

times_S = np.array(times_S)
times_R = np.array(times_R)
times_T = np.array(times_T)
resdevS = np.array(resdevS)
resdevR = np.array(resdevR)
resdevT = np.array(resdevT)

plt.title("Time Requirements")
plt.plot(K, times_S[:,-1], label="Simpson")
plt.plot(K, times_R[:,-1], label="Romberg")
plt.plot(K, times_T[:,-1], label="Trapezoid")
plt.plot(K, [tquad for k in K], label="default quadrature")
plt.plot(K, times_S[:,1], "b.", label="Simpson, integration only")
plt.plot(K, times_R[:,1], "y.", label="Romberg, integration only")
plt.plot(K, times_T[:,1], "g.", label="Trapezoid, integration only")
plt.legend()
plt.yscale('log')
plt.xlabel("number of support points log(N)")
plt.ylabel("time in s")
plt.show()

plt.title("Deviation from exact result")
plt.plot(K, resdevS[:,-1], label="Simpson")
plt.plot(K, resdevR[:,-1], label="Romberg")
plt.plot(K, resdevT[:,-1], label="Trapezoid")
plt.plot(K, [accuracy for k in K], label="default quadrature")
plt.legend()
plt.yscale('log')
plt.xlabel("number of support points log(N)")
plt.ylabel("absolute error")
plt.show()

plt.title("Function Value")
plt.plot(K, resdevS[:,0], label="Simpson")
plt.plot(K, resdevR[:,0], label="Romberg")
plt.plot(K, resdevT[:,0], label="Trapezoid")
plt.plot(K, [exact for k in K], label="default quadrature")
plt.legend()
plt.xlabel("number of support points log(N)")
plt.ylabel("function value")
plt.show()

