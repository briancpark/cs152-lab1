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