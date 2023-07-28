import numpy as np
import matplotlib.pyplot as plt


colormaps = [
    "viridis",
    "inferno",
    "cividis"
]


gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

plt.rcParams['font.family'] = 'TeX Gyre Heros'
plt.rcParams['figure.constrained_layout.w_pad'] = 0.0
plt.rcParams['figure.constrained_layout.h_pad'] = 0.01


n_rows = len(colormaps)
fig, axs = plt.subplots(n_rows, figsize=(62 / 25.4, 12 / 25.4), layout="constrained")

for ax, cmap in zip(axs, colormaps):
    ax.imshow(gradient, aspect='auto', cmap=cmap)
    ax.text(
        -0.01, 0.5,
        cmap,
        va='center',
        ha='right',
        fontsize=8,
        transform=ax.transAxes
    )

for ax in axs:
    ax.set_axis_off()

fig.savefig("build/cmaps.pdf")

