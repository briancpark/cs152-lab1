# CS 152 Logs and Commands for Lab 1

## Getting Started

Make sure these commands are run and environment variables are set upon login:

```sh
source ~cs152/sp22/cs152.lab1.bashrc
```

```sh
cd /scratch/$USER
LAB1ROOT=$PWD
BMARKS=$LAB1ROOT/generators/riscv-sodor/riscv-bmarks
SCRIPTS=$LAB1ROOT/generators/riscv-sodor/scripts
./scripts/init-submodules-no-riscv-tools.sh
```

Compile a simulator:

```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig
```

Running benchmarks on different configurations of pipeline:

1. 1-stage pipeline

```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig run-binary BINARY=${BMARKS}/towers.riscv
```

```
mcycle = 6166
minstret = 6172
```

2. 2-stage pipeline

```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor2StageConfig run-binary BINARY=${BMARKS}/towers.riscv
```

```
mcycle = 6582
minstret = 6172
```

3. 3-stage pipeline

```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor3StageConfig run-binary BINARY=${BMARKS}/towers.riscv
```

```
mcycle = 7414
minstret = 6172
```

4. 5-stage pipeline

```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/towers.riscv
```

```
mcycle = 7000
minstret = 6172
```

5. UCode pipeline
```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=SodorUCodeConfig run-binary BINARY=${BMARKS}/towers.riscv
```

```
mcycle = 45051
minstret = 6172
```

## CPI Analysis Using the 1-Stage Processor

### dhrystone

```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig run-binary BINARY=${BMARKS}/dhrystone.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor1StageConfig/dhrystone.out
```

```
Microseconds for one run through Dhrystone: 449
Dhrystones per Second:                      2227
mcycle = 224524
minstret = 224530

Stats:

CPI          : 1.000
IPC          : 1.000
Cycles       : 245699
Instructions : 245700
Bubbles      : 0

Instruction Breakdown:
% Arithmetic  : 40.381 %
% Ld/St       : 35.321 %
% Branch/Jump : 23.757 %
% Misc.       : 0.541 %
```

### median

```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig run-binary BINARY=${BMARKS}/median.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor1StageConfig/median.out
```

```
mcycle = 4149
minstret = 4155

Stats:

CPI          : 1.000
IPC          : 1.000
Cycles       : 17180
Instructions : 17181
Bubbles      : 0

Instruction Breakdown:
% Arithmetic  : 31.843 %
% Ld/St       : 32.158 %
% Branch/Jump : 35.184 %
% Misc.       : 0.815 %
```

### multiply

```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig run-binary BINARY=${BMARKS}/multiply.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor1StageConfig/multiply.out
```

```
mcycle = 20896
minstret = 20902

Stats:

CPI          : 1.000
IPC          : 1.000
Cycles       : 50611
Instructions : 50612
Bubbles      : 0

Instruction Breakdown:
% Arithmetic  : 63.157 %
% Ld/St       : 4.876 %
% Branch/Jump : 31.619 %
% Misc.       : 0.348 %
```

### qsort

```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig run-binary BINARY=${BMARKS}/qsort.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor1StageConfig/qsort.out
```

```
mcycle = 123503
minstret = 123509

Stats:

CPI          : 1.000
IPC          : 1.000
Cycles       : 236654
Instructions : 236655
Bubbles      : 0

Instruction Breakdown:
% Arithmetic  : 38.379 %
% Ld/St       : 31.473 %
% Branch/Jump : 29.825 %
% Misc.       : 0.322 %
```

### rsort

```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig run-binary BINARY=${BMARKS}/rsort.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor1StageConfig/rsort.out
```

```
mcycle = 171128
minstret = 171134

Stats:

CPI          : 1.000
IPC          : 1.000
Cycles       : 375281
Instructions : 375282
Bubbles      : 0

Instruction Breakdown:
% Arithmetic  : 59.575 %
% Ld/St       : 34.872 %
% Branch/Jump : 4.401 %
% Misc.       : 1.152 %
```

### towers

```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig run-binary BINARY=${BMARKS}/towers.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor1StageConfig/towers.out
```

```
mcycle = 6166
minstret = 6172

Stats:

CPI          : 1.000
IPC          : 1.000
Cycles       : 19591
Instructions : 19592
Bubbles      : 0

Instruction Breakdown:
% Arithmetic  : 41.716 %
% Ld/St       : 42.180 %
% Branch/Jump : 15.389 %
% Misc.       : 0.715 %
```

### vvadd

```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig run-binary BINARY=${BMARKS}/vvadd.riscv
less output/chipyard.TestHarness.Sodor1StageConfig/vvadd.out
```

```sh
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor1StageConfig/vvadd.out
```

```
mcycle = 2412
minstret = 2418

Stats:

CPI          : 1.000
IPC          : 1.000
Cycles       : 12946
Instructions : 12947
Bubbles      : 0

Instruction Breakdown:
% Arithmetic  : 45.887 %
% Ld/St       : 30.548 %
% Branch/Jump : 22.484 %
% Misc.       : 1.081 %
```


## CPI Analysis Using the 5-Stage Processor

Benchmarks with full bypassing on.
### dhrystone

```sh
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/dhrystone.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/dhrystone.out
```

```
Microseconds for one run through Dhrystone: 589
Dhrystones per Second:                      1697
mcycle = 294534
minstret = 224530

Stats:

CPI          : 1.323
IPC          : 0.756
Cycles       : 321980
Instructions : 243405
Bubbles      : 78576

Instruction Breakdown:
% Arithmetic  : 40.530 %
% Ld/St       : 35.199 %
% Branch/Jump : 23.725 %
% Misc.       : 0.546 %
```

### median

```sh
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/median.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/median.out
```

```
mcycle = 6369
minstret = 4155


Stats:

CPI          : 1.469
IPC          : 0.681
Cycles       : 24257
Instructions : 16513
Bubbles      : 7745

Instruction Breakdown:
% Arithmetic  : 32.471 %
% Ld/St       : 31.387 %
% Branch/Jump : 35.293 %
% Misc.       : 0.848 %
```

### multiply

```sh
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/multiply.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/multiply.out
```

```
mcycle = 33136
minstret = 20902

Stats:

CPI          : 1.565
IPC          : 0.639
Cycles       : 78272
Instructions : 50012
Bubbles      : 28261

Instruction Breakdown:
% Arithmetic  : 63.801 %
% Ld/St       : 4.227 %
% Branch/Jump : 31.620 %
% Misc.       : 0.352 %
```

### qsort

```sh
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/qsort.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/qsort.out
```

```
mcycle = 172780
minstret = 123509

Stats:

CPI          : 1.421
IPC          : 0.704
Cycles       : 335271
Instructions : 236006
Bubbles      : 99266

Instruction Breakdown:
% Arithmetic  : 38.448 %
% Ld/St       : 31.404 %
% Branch/Jump : 29.826 %
% Misc.       : 0.323 %
```

### rsort

```sh
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/rsort.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/rsort.out
```

```
mcycle = 182392
minstret = 171134

Stats:

CPI          : 1.083
IPC          : 0.923
Cycles       : 405570
Instructions : 374490
Bubbles      : 31081

Instruction Breakdown:
% Arithmetic  : 59.660 %
% Ld/St       : 34.844 %
% Branch/Jump : 4.341 %
% Misc.       : 1.155 %
```

### towers

```sh
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/towers.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/towers.out
```

```
mcycle = 7000
minstret = 6172

Stats:

CPI          : 1.250
IPC          : 0.800
Cycles       : 23604
Instructions : 18877
Bubbles      : 4728

Instruction Breakdown:
% Arithmetic  : 42.544 %
% Ld/St       : 41.935 %
% Branch/Jump : 14.780 %
% Misc.       : 0.742 %
```

### vvadd

```sh
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/vvadd.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/vvadd.out
```

```
mcycle = 3020
minstret = 2418

Stats:

CPI          : 1.351
IPC          : 0.740
Cycles       : 16519
Instructions : 12229
Bubbles      : 4291

Instruction Breakdown:
% Arithmetic  : 47.535 %
% Ld/St       : 29.397 %
% Branch/Jump : 21.923 %
% Misc.       : 1.145 %
```

Below is the benchmarks with full bypassing off.

### dhrystone

```sh
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/dhrystone.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/dhrystone.out
```

```
Microseconds for one run through Dhrystone: 890
Dhrystones per Second:                      1123
mcycle = 445046
minstret = 224530

Stats:

CPI          : 1.986
IPC          : 0.504
Cycles       : 481120
Instructions : 242300
Bubbles      : 238821

Instruction Breakdown:
% Arithmetic  : 40.631 %
% Ld/St       : 35.091 %
% Branch/Jump : 23.729 %
% Misc.       : 0.549 %
```

### median

```sh
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/median.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/median.out
```

```
mcycle = 7980
minstret = 4155

Stats:

CPI          : 1.888
IPC          : 0.530
Cycles       : 30462
Instructions : 16137
Bubbles      : 14326

Instruction Breakdown:
% Arithmetic  : 32.732 %
% Ld/St       : 30.855 %
% Branch/Jump : 35.546 %
% Misc.       : 0.868 %
```

### multiply

```sh
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/multiply.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/multiply.out
```

```
mcycle = 39639
minstret = 20902

Stats:

CPI          : 1.911
IPC          : 0.523
Cycles       : 94916
Instructions : 49679
Bubbles      : 45238

Instruction Breakdown:
% Arithmetic  : 64.126 %
% Ld/St       : 3.889 %
% Branch/Jump : 31.631 %
% Misc.       : 0.354 %
```

### qsort

```sh
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/qsort.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/qsort.out
```

```
mcycle = 237844
minstret = 123509

Stats:

CPI          : 1.935
IPC          : 0.517
Cycles       : 456086
Instructions : 235660
Bubbles      : 220427

Instruction Breakdown:
% Arithmetic  : 38.475 %
% Ld/St       : 31.363 %
% Branch/Jump : 29.839 %
% Misc.       : 0.323 %
```

### rsort

```sh
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/rsort.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/rsort.out
```

```
mcycle = 407783
minstret = 171134

Stats:

CPI          : 2.323
IPC          : 0.430
Cycles       : 869558
Instructions : 374326
Bubbles      : 495233

Instruction Breakdown:
% Arithmetic  : 59.696 %
% Ld/St       : 34.806 %
% Branch/Jump : 4.342 %
% Misc.       : 1.155 %
```

### towers

```sh
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/towers.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/towers.out
```

```
mcycle = 9159
minstret = 6172

Stats:

CPI          : 1.673
IPC          : 0.598
Cycles       : 30977
Instructions : 18518
Bubbles      : 12460

Instruction Breakdown:
% Arithmetic  : 42.996 %
% Ld/St       : 41.657 %
% Branch/Jump : 14.591 %
% Misc.       : 0.756 %
```

### vvadd

```sh
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/vvadd.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/vvadd.out
```

```
mcycle = 4223
minstret = 2418

Stats:

CPI          : 1.839
IPC          : 0.544
Cycles       : 21921
Instructions : 11917
Bubbles      : 10005

Instruction Breakdown:
% Arithmetic  : 48.208 %
% Ld/St       : 28.623 %
% Branch/Jump : 21.994 %
% Misc.       : 1.175 %
```


## 3.7
### dhrystone
Stats:

CPI          : 0.876
IPC          : 1.142
Cycles       : 245699
Instructions : 280579
Bubbles      : 0

Instruction Breakdown:
% Arithmetic   : 47.792 %
% Ld/St        : 30.930 %
% Ld/St Nonzero : 12.431 %
% Branch/Jump  : 20.803 %
% Misc.        : 0.474 %


Stats:

CPI          : 0.857
IPC          : 1.167
Cycles       : 17180
Instructions : 20056
Bubbles      : 0

Instruction Breakdown:
% Arithmetic   : 41.613 %
% Ld/St        : 27.548 %
% Ld/St Nonzero : 14.335 %
% Branch/Jump  : 30.141 %
% Misc.        : 0.698 %


Stats:

CPI          : 0.979
IPC          : 1.021
Cycles       : 50611
Instructions : 51697
Bubbles      : 0

Instruction Breakdown:
% Arithmetic   : 63.930 %
% Ld/St        : 4.774 %
% Ld/St Nonzero : 2.099 %
% Branch/Jump  : 30.955 %
% Misc.        : 0.340 %


Stats:

CPI          : 0.974
IPC          : 1.027
Cycles       : 236654
Instructions : 242932
Bubbles      : 0

Instruction Breakdown:
% Arithmetic   : 39.972 %
% Ld/St        : 30.660 %
% Ld/St Nonzero : 2.584 %
% Branch/Jump  : 29.055 %
% Misc.        : 0.314 %


Stats:

CPI          : 0.953
IPC          : 1.049
Cycles       : 375281
Instructions : 393828
Bubbles      : 0

Instruction Breakdown:
% Arithmetic   : 61.478 %
% Ld/St        : 33.230 %
% Ld/St Nonzero : 4.709 %
% Branch/Jump  : 4.194 %
% Misc.        : 1.098 %


Stats:

CPI          : 0.764
IPC          : 1.309
Cycles       : 19591
Instructions : 25650
Bubbles      : 0

Instruction Breakdown:
% Arithmetic   : 55.481 %
% Ld/St        : 32.218 %
% Ld/St Nonzero : 23.618 %
% Branch/Jump  : 11.754 %
% Misc.        : 0.546 %


Stats:

CPI          : 0.916
IPC          : 1.092
Cycles       : 12946
Instructions : 14139
Bubbles      : 0

Instruction Breakdown:
% Arithmetic   : 50.449 %
% Ld/St        : 27.972 %
% Ld/St Nonzero : 8.431 %
% Branch/Jump  : 20.588 %
% Misc.        : 0.990 %


cd ${LAB1ROOT}/generators/riscv-sodor/test/custom-bmarks && make && make run && cd ${LAB1ROOT}/sims/verilator && CUSTOM_BMARKS=${LAB1ROOT}/generators/riscv-sodor/test/custom-bmarks && make CONFIG=Sodor5StageConfig run-binary BINARY=${CUSTOM_BMARKS}/mix.riscv && ${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor5StageConfig/mix.out