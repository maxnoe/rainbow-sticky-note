import matplotlib.pyplot as plt
import numpy as np

radius = 0.95
lw = 25

gradient = np.linspace(0, 1, 256).reshape((1, 256))

fig = plt.figure(figsize=(3, 3))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_aspect(1)
ax.set_axis_off()
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

cax = fig.add_axes([0.1, 0.4, 0.8, 0.2], zorder=-1)
cax.imshow(gradient, cmap='jet')
cax.set_aspect('auto')
cax.set_axis_off()


circle = plt.Circle(radius=radius, xy=(0, 0), edgecolor='xkcd:red', facecolor='none', linewidth=lw)
ax.add_patch(circle)


p = 0.95 * np.sin(np.pi / 4) * np.array([-radius, radius])
ax.plot(p, p, 'xkcd:red', linewidth=lw)

fig.savefig('build/norainbow.pdf')
