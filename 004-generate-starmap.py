from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

# =========================================================================== #
# generate star map
N_seeds = 10                    # this many randomly chosen coordinates. Set to 1 to see the effect of the other params
N_waves = 4                     # generate this many rings of stars around the randomly created ones
l_wave  = .3                    # each ring has k * l_wave, where k is an int in range(1, N_waves + 1)
N_pointsPerWave = 30            # each ring comprises of this many stars

points = np.random.uniform( size=(N_seeds, 2) )
stars = np.copy(points)

for point in points :
    for k in range(N_waves) :
        orientations = np.random.uniform(0, 2 * np.pi, N_pointsPerWave)
        
        l = (k + 1) * l_wave
        offsets = l * np.array((np.cos(orientations), np.sin(orientations))).T
        
        stars = np.insert(stars, -1, point + offsets, axis=0)

plt.figure()
plt.plot(stars[:,0], stars[:,1], '.')
plt.plot()

# =========================================================================== #
# generate the density map
# we count only the stars within [xmin, xmax] x [ymin, ymax]
# density = N / volume, where volume is vol([xmin, xmax] x [ymin, ymax])

window = lambda point, xmin = 0, xmax = 1, ymin = 0, ymax = 1: \
    (xmin <= point[0] <= xmax) and (ymin <= point[1] <= ymax)

mask = [window(star) for star in stars]
windowStars = stars[mask]
rhoMean = windowStars.size          # vol = 1

xStep = .02
yStep = .02

X = np.arange(0, 1, xStep)
Y = np.arange(0, 1, yStep)

mask = np.array(
        [[[window(star, xmin, xmin + xStep, ymin, ymin + yStep)
                for star in stars]
                for xmin in X]
                for ymin in Y]
    )

density = np.array([[
        stars[mask[i, j]].size 
         for j in range(len(X)) ] 
         for i in range(len(Y))
    ]) / (xStep * yStep)

mesh = np.meshgrid(X, Y)

plt.figure()
plt.pcolor(X, Y, density, shading='auto')
plt.plot()

# =========================================================================== #
# transform into contrast.
# contrast is simply relative deviation from the regional mean

contrast = (density / rhoMean) - 1

plt.figure()
plt.pcolor(X, Y, contrast, shading='auto')
plt.plot()

print( np.min(contrast), np.max(contrast) )

# =========================================================================== #
# correlation

corr = signal.correlate(contrast, contrast)
