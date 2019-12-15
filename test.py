import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
x3 = np.linspace(0.0, 1.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)
y3 = np.cos(np.pi * x3)

# Create three subplots sharing x axis
fig, (ax1, ax2, ax3) = plt.subplots(
    nrows=1, ncols=3)  # sharex=False, sharey=False
# Create three subplots sharing y axis
# fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)
ax1.plot(x1, y1, 'ko-')
ax1.set(title='A tale of 3 subplots', xlabel='K', ylabel='Distance')

ax2.plot(x2, y2, 'r.-')
ax2.set(xlabel='K', ylabel='Local Clustering')
ax2.plot(x3, y3, 'r.-')

ax3.plot(x3, y3, 'r.-')
ax3.set(xlabel='K', ylabel='Average')

plt.show()
