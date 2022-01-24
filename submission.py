import numpy as np
import matplotlib.pyplot as plt


### 3.4
benchmarks = ["dhrystone", "median", "multiply", "qsort", "rsort", "towers", "vvadd"]
arithmetic = [40.381, 31.843, 63.157, 38.379, 59.575, 41.716, 45.887]
memory = [35.321, 32.158, 4.876, 31.473, 34.872, 42.180, 30.548]
control = [23.757, 35.184, 31.619, 29.825, 4.401, 15.389, 22.484]
misc = [0.541, 0.815, 0.348, 0.322, 1.152, 0.715, 1.081]

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
plt.savefig("figures/3_4.png")
plt.clf()




"""
Consider the results gathered from the RV32 1-stage processor. 
Suppose you were to design a new machine such that the average CPI of loads and stores 
is 2 cycles, integer arithmetic instructions take 1 cycle, and other instructions take 
1.5 cycles on average. What is the overall CPI of the machine for each benchmark?

What is the relative performance for each benchmark if loads/stores are sped up to 
have an average CPI of 1? Is this still a worthwhile modification if it means that the
cycle time increases 30\%? Is it worthwhile for all benchmarks or only a subset? Explain.
"""

### 3.5

new_arithmetic = [1 * x for x in arithmetic]
new_memory = [2 * x for x in memory]
new_control = [1.5 * x for x in control]
new_misc = [1.5 * x for x in misc]

for i in range(len(benchmarks)):
    total = new_arithmetic[i] + new_memory[i] + new_control[i] + new_misc[i]
    new_arithmetic[i] = new_arithmetic[i] / total
    new_memory[i] = new_memory[i] / total
    new_control[i] = new_control[i] / total
    new_misc[i] = new_misc[i] / total
    
plt.figure(figsize=(10, 5), dpi=440)

plt.bar(X_axis - 0.2, new_arithmetic, 0.2, label="Arithmetic")
plt.bar(X_axis, new_memory, 0.2, label="Memory")
plt.bar(X_axis + 0.2, new_control, 0.2, label="Control")

plt.title("Benchmark by Instruction Breakdown Modified")
plt.xticks(X_axis, benchmarks)
plt.xlabel("Benchmarks")
plt.ylabel("Intensity (%)")
plt.legend()
plt.savefig("figures/3_5.png")
plt.clf()