import numpy as np
import matplotlib.pyplot as plt

### 3.4
benchmarks = ["dhrystone", "median", "multiply", "qsort", "rsort", "towers", "vvadd"]
arithmetic = [40.381, 31.843, 63.157, 38.379, 59.575, 41.716, 45.887]
memory = [35.321, 32.158, 4.876, 31.473, 34.872, 42.180, 30.548]
control = [23.757, 35.184, 31.619, 29.825, 4.401, 15.389, 22.484]
misc = [0.541, 0.815, 0.348, 0.322, 1.152, 0.715, 1.081]
instructions = [245700, 17181, 50612, 236655, 375282, 19592, 12947]
cycles = [instruction - 1 for instruction in instructions]

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

### 3.5

new_cpi = []

print("Benchmarks for Modified CPI")
for i in range(len(benchmarks)):
    total_cycles = 0
    total_cycles += int(arithmetic[i] * cycles[i])
    total_cycles += int(2 * memory[i] * cycles[i])
    total_cycles += int(1.5 * control[i] * cycles[i])
    total_cycles += int(1.5 * misc[i] * cycles[i])
    new_cpi.append(total_cycles / instructions[i] / 100)
    print(f"{benchmarks[i]} & {round(new_cpi[i], 3)}")

plt.figure(figsize=(10, 5), dpi=440)
plt.bar(benchmarks, new_cpi)
plt.title("New CPI for Benchmarks")
plt.xlabel("Benchmarks")
plt.ylabel("CPI")
plt.savefig("figures/3_5_1.png")
plt.clf()


new_cpi_mem = []

print("Benchmarks for Modified CPI")
for i in range(len(benchmarks)):
    total_cycles = 0
    total_cycles += int(arithmetic[i] * cycles[i])
    total_cycles += int(memory[i] * cycles[i])
    total_cycles += int(1.5 * control[i] * cycles[i])
    total_cycles += int(1.5 * misc[i] * cycles[i])
    new_cpi_mem.append(total_cycles / instructions[i] / 100)
    print(f"{benchmarks[i]} & {round(new_cpi[i], 3)}")

plt.figure(figsize=(10, 5), dpi=440)
plt.bar(benchmarks, new_cpi)
plt.title("New CPI for Benchmarks")
plt.xlabel("Benchmarks")
plt.ylabel("CPI")
plt.savefig("figures/3_5_2.png")
plt.clf()

# Comparison Plot
plt.figure(figsize=(10, 5), dpi=440)
plt.bar(X_axis - 0.2, new_cpi, 0.4, label="Modified CPI")
plt.bar(X_axis + 0.2, new_cpi_mem , 0.4, label="Mofiied CPI with Memory Optimized")
plt.title("CPI Comparison")
plt.xticks(X_axis, benchmarks)
plt.xlabel("Benchmarks")
plt.ylabel("CPI")
plt.legend(loc='lower right')
plt.savefig("figures/3_5_3.png")
plt.clf()