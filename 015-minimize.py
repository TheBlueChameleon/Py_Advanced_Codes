import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#X = np.linspace(-2, 5, 100)
#Xdistinct = np.random.choice( X, 10 )
#
#coeffsTrue = (3, -1)
#pTrue = np.polynomial.Polynomial( coeffsTrue )
#YTrueDistinct = pTrue(Xdistinct)
#
#coeffs1 = (2.9, -1.5)
#coeffs2 = (3.5, -0.5)
#coeffs3 = (1.9, -1.0)
#
#p1 = np.polynomial.Polynomial( coeffs1 )
#p2 = np.polynomial.Polynomial( coeffs2 )
#p3 = np.polynomial.Polynomial( coeffs3 )
#
#def avgCost (m, t) :
#    cost = 0
#    p = np.polynomial.Polynomial( (t, m) )
#    for x in Xdistinct :
#        cost += (p(x) - pTrue(x))**2
#    return cost / len(Xdistinct)
#
#M, T = np.meshgrid( np.linspace(-2, 2, 100), np.linspace(1, 5, 100) )
#C = np.zeros_like( M )
#
#for i, j in np.ndindex(M.shape) :
#    C[i, j] = avgCost( M[i, j], T[i, j] )
#
#fig = plt.figure( figsize=(16, 8) )
#
#drwFit = fig.add_subplot(121)
#drwCst = fig.add_subplot(122)
#
#drwFit.set_title("Data and Fits\n$y = mx + t$")
#drwFit.set_xlabel("x")
#drwFit.set_ylabel("y")
#
#drwFit.plot(Xdistinct, YTrueDistinct, linestyle="", marker=".", label="Training Data (m={}, t={})".format(*coeffsTrue))
#drwFit.plot(X, p1(X), label="Guess 1 (t={}, m={})".format(*coeffs1) )
#drwFit.plot(X, p2(X), label="Guess 2 (t={}, m={})".format(*coeffs2) )
#drwFit.plot(X, p3(X), label="Guess 3 (t={}, m={})".format(*coeffs3) )
#
#drwFit.legend()
#
#drwCst.set_title("Parameters and Cost\nAverage Distance Squared")
#drwCst.set_xlabel("m")
#drwCst.set_ylabel("t")
#
#plt.set_cmap('turbo')
#d = drwCst.pcolor( M, T, C )
#plt.colorbar(d)
#
#plt.show()


#X = np.linspace(-2, 5, 100)
#coeffs = (3, 5, 6, -6, 1)
#p = np.polynomial.Polynomial( coeffs )
#dp = p.deriv()
#Y = p(X)
#
#X1 = -1.5
#Y1 = p(X1)
#
#X2 = 4.5
#Y2 = p(X2)
#
#fig = plt.figure( figsize=(8, 8) )
#
#plt.plot(X, Y)
#plt.plot(X1, Y1, color='red'  , marker='D')
#plt.plot(X2, Y2, color='green', marker='D')
#
#plt.show()

coeffsX = (+0, +17, -10, -5, +3)
coeffsY = (+0, +17, -10, -5, +3)

X, Y = np.meshgrid( np.linspace(-2.0, 2.5, 80), np.linspace(-2, 2.5, 80) )

Z = np.zeros_like(X)
for n, a in enumerate(coeffsX) :
    Z += a * X**n

for n, a in enumerate(coeffsY) :
    Z += a * Y**n
    
fig = plt.figure( figsize=(16, 8) )
drwL = fig.add_subplot(121, projection='3d')
drwR = fig.add_subplot(122)

drwL.plot_surface(X, Y, Z)
drwL.set_xlabel('a')
drwL.set_ylabel('b')
drwL.view_init(60, -60)

drwR.pcolor(X, Y, Z, shading='auto')
drwR.set_xlabel('a')
drwR.set_ylabel('b')

#drwL.set_title("Potential Landscape")
plt.show()