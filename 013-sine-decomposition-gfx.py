#!/bin/python3

#import matplotlib.pyplot as plt
#import numpy as np
#
#X = np.linspace(0, 2*np.pi, 300)
#
#Y1 = np.sin(X)
#Y2 = 1.0 * np.sin(1*X) +  0.3 * np.sin(5*X)
#
#fig = plt.figure( figsize=(6, 12) )
#
#drw1 = fig.add_subplot(211)
#drw2 = fig.add_subplot(212)
#
#drw1.plot(X, Y1)
#drw2.plot(X, Y2)
#
#fig.show()


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


X = np.linspace(0, 2*np.pi, 300)

Y1 = np.sin(X)

fig = plt.figure( figsize=(6, 12) )

drw1 = fig.add_subplot(211)
drw2 = fig.add_subplot(212, projection='3d')

drw1.plot(X, Y1, label="sin(x)")
drw1.plot(X, [0 for x in X], 'black')
drw1.plot([1.0, 1.0], [0, np.sin(1.0)], label="x")
drw1.plot([2.5, 2.5], [0, np.sin(2.5)], label="y")
drw1.plot([4.5, 4.5], [0, np.sin(4.5)], label="z")
drw1.legend()

drw2.plot([        0  , np.sin(1.0)], [        0  ,np.sin(2.5)], [0,np.sin(4.5)], label='"sin(x)"')
drw2.plot([        0  , np.sin(1.0)], [        0  ,        0  ], [0,        0  ])
drw2.plot([np.sin(1.0), np.sin(1.0)], [        0  ,np.sin(2.5)], [0,        0  ])
drw2.plot([np.sin(1.0), np.sin(1.0)], [np.sin(2.5),np.sin(2.5)], [0,np.sin(4.5)])

drw2.set_xlabel('x')
drw2.set_ylabel('y')
drw2.set_zlabel('z')

drw2.legend()

fig.show()


#import matplotlib.pyplot as plt
#import numpy as np
#
#X = np.linspace(0, 2*np.pi, 300)
#Y = np.sin(X)
#
#h = 0.5
#x = (np.pi / 2) - h
#t = slice(0, 100)
#r = slice(0, 150)
#
#m = (np.sin(x + h) - np.sin(  x  )) /   h
#c = (np.sin(x + h) - np.sin(x - h)) / (2*h)
#
#T = [np.cos(x) * (t - x) + np.sin(x) for t in X]
#S = [   m      * (t - x) + np.sin(x) for t in X]
#C = [   c      * (t - x) + np.sin(x) for t in X]
#
#plt.figure()
#
#plt.plot(X[r], S[r], color='blue' , label="Secant, forward")
#plt.plot(X[r], C[r], color='green', label="Secant, central")
#plt.plot(X[t], T[t], color='red'  , label="Tangent")
#plt.plot(X, Y)
#plt.plot([  x  ], [np.sin(  x  )], marker='o', linestyle='none', color='red' )
#plt.plot([x + h], [np.sin(x + h)], marker='o', linestyle='none', color='blue')
#plt.plot([x - h], [np.sin(x - h)], marker='o', linestyle='none', color='green')
#
#plt.plot([x  , x  ], [np.sin( x ), -0.5], linewidth=1, color='black')
#plt.plot([x+h, x+h], [np.sin(x+h), -0.5], linewidth=1, color='black')
#
#plt.annotate('←h→', xy=(x + .05, -.4))
#
#plt.legend()
#plt.show()
