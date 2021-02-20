from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# this essentially implements y'' = -y
def dv (t, x_vec) :
    x2, x1, x0 = x_vec
    x3 = -x1
    return [x3, x2, x1]

P = 10
N = 10 * P
t = np.linspace(0, P * np.pi, N)
y0 = [0, 1, 0]

sol = odeint(dv, y0, t, tfirst=True)

print(sol.shape)

plt.figure()
plt.plot(t, sol[:,0])
plt.plot(t, sol[:,1])
plt.plot(t, sol[:,2])
plt.show()