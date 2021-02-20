import scipy
import numpy as np
import matplotlib.pyplot as plt


N_seeds = 10
N_pointsPerWave = 100
N_waves = 3
l_wave  = .3

points = np.random.uniform( size=(N_seeds, 2) )
stars = np.copy(points)

for point in points :
    for k in range(N_waves) :
        orientations = np.random.uniform(0, 2 * np.pi, N_pointsPerWave)
        
        l = (k + 1) * l_wave
        offsets = l * np.array((np.cos(orientations), np.sin(orientations))).T
        
        stars = np.insert(stars, -1, point + offsets, axis=0)
        
distances = [ np.sqrt(np.sum( (x-y)**2 )) for x in stars for y in stars ]
hist = np.histogram(distances)
print(distances)

print("STARS\n", stars)
#print("DISTANCES\n", distances)

plt.figure()
plt.plot(stars[:,0], stars[:,1], 'o')
plt.plot()

plt.figure()
plt.hist( distances )
plt.plot()