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

new_cpi_mem = [cpi * 1.3 for cpi in new_cpi_mem]
# Comparison Plot
plt.figure(figsize=(10, 5), dpi=440)
plt.bar(X_axis - 0.2, new_cpi, 0.4, label="Modified CPI")
plt.bar(
    X_axis + 0.2,
    new_cpi_mem,
    0.4,
    label="Modified CPI with Memory Optimized and Increased Cycle Time of 30%",
)
plt.title("CPI Comparison")
plt.xticks(X_axis, benchmarks)
plt.xlabel("Benchmarks")
plt.ylabel("CPI")
plt.legend(loc="lower right")
plt.savefig("figures/3_5_3.png")
plt.clf()


### 3.6

cpi_bypass_on = [1.323, 1.469, 1.565, 1.421, 1.083, 1.250, 1.351]
cpi_bypass_off = [1.986, 1.888, 1.911, 1.935, 2.323, 1.673, 1.839]

print("Percentage Slowdown for Bypass")
for i in range(len(benchmarks)):
    print(f"{benchmarks[i]} & {round(cpi_bypass_on[i] / cpi_bypass_off[i], 3)}")

plt.figure(figsize=(10, 5), dpi=440)
plt.bar(X_axis - 0.2, cpi_bypass_on, 0.4, label="Full Bypassing")
plt.bar(X_axis + 0.2, cpi_bypass_off, 0.4, label="Full Interlocking")
plt.title("CPI Comparison of 5-Stage Pipeline Full Bypassing vs. Full Interlocking")
plt.xticks(X_axis, benchmarks)
plt.xlabel("Benchmarks")
plt.ylabel("CPI")
plt.legend()
plt.savefig("figures/3_6.png")
plt.clf()


### 3.7
benchmarks = ["dhrystone", "median", "multiply", "qsort", "rsort", "towers", "vvadd"]
arithmetic = [47.792, 41.613, 63.930, 39.972, 61.478, 55.481, 50.449]
memory = [30.930, 27.548, 4.774, 30.660, 33.230, 32.218, 27.972]
memory_nz = [12.431, 14.335, 2.099, 2.584, 4.709, 23.618, 8.431]
control = [20.803, 30.141, 30.955, 29.055, 4.194, 11.754, 20.588]
misc = [0.474, 0.698, 0.340, 0.314, 1.098, 0.546, 0.990]


nz_instructions = [280579, 20056, 51697, 242932, 393828, 25650, 14139]

X_axis = np.arange(len(benchmarks))


plt.figure(figsize=(10, 5), dpi=440)

plt.bar(X_axis - 0.15, arithmetic, 0.1, label="Arithmetic")
plt.bar(X_axis - 0.05, memory, 0.1, label="Memory")
plt.bar(X_axis + 0.05, memory_nz, 0.1, label="Memory Non-Zero Offsets")
plt.bar(X_axis + 0.15, control, 0.1, label="Control")

plt.title("Benchmark by Instruction Breakdown")
plt.xticks(X_axis, benchmarks)
plt.xlabel("Benchmarks")
plt.ylabel("Intensity (%)")
plt.legend()
plt.savefig("figures/3_7_1.png")
plt.clf()


plt.figure(figsize=(10, 5), dpi=440)
plt.bar(X_axis - 0.2, instructions, 0.4, label="Original")
plt.bar(X_axis + 0.2, nz_instructions, 0.4, label="Modified for Non-Zero Offsets")
plt.title("Instructions Comparison")
plt.xticks(X_axis, benchmarks)
plt.xlabel("Benchmarks")
plt.ylabel("Instructions")
plt.legend(loc="upper right")
plt.savefig("figures/3_7_2.png")
plt.clf()

print([nz_instruction / instruction for instruction, nz_instruction in zip(instructions, nz_instructions)])