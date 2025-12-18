import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

distances_bad = np.load("dist_bad.npy")
distances_inv = np.load("dist_inv.npy")

plt.plot(distances_bad)
plt.plot(distances_inv)
plt.savefig("invariance_comparison.png", dpi=300)
