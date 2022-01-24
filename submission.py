import numpy as np
import matplotlib.pyplot as plt


### 3.4
benchmarks = ["dhrystone", "median", "multiply", "qsort", "rsort", "towers", "vvadd"]
arithmetic = [40.381, 31.843, 63.157, 38.379, 59.575, 41.716, 45.887]
memory = [35.321, 32.158, 4.876, 31.473, 34.872, 42.180, 30.548]
control = [23.757, 35.184, 31.619, 29.825, 4.401, 15.389, 22.484]

X_axis = np.arange(len(benchmarks))


plt.figure(figsize=(10, 5), dpi=440)

plt.bar(X_axis - 0.2, arithmetic, 0.2, label="Arithmetic")
plt.bar(X_axis, memory, 0.2, label="Memory")
plt.bar(X_axis + 0.2, control, 0.2, label="Control")

plt.title("Benchmark by Instruction Breakdown")
plt.xticks(X_axis, benchmarks)
plt.xlabel("Benchmarks")
plt.ylabel("Intensity (%)")
plt.legend()
plt.savefig("figures/lab1.png")
