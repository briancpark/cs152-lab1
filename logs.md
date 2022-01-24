# CS 152 Logs and Commands for Lab 1

## Getting Started
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

```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig
```

```sh
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig run-binary BINARY=${BMARKS}/towers.riscv
```

## Results
mcycle = 6166
minstret = 6172

cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor2StageConfig run-binary BINARY=${BMARKS}/towers.riscv

mcycle = 6582
minstret = 6172

cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor3StageConfig run-binary BINARY=${BMARKS}/towers.riscv

mcycle = 7414
minstret = 6172

cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor5StageConfig run-binary BINARY=${BMARKS}/towers.riscv

mcycle = 7000
minstret = 6172

cd ${LAB1ROOT}/sims/verilator
make CONFIG=SodorUCodeConfig run-binary BINARY=${BMARKS}/towers.riscv
mcycle = 45051
minstret = 6172

## Benchmarking

# dhrystone

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


# median
```
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

# multiply
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig run-binary BINARY=${BMARKS}/multiply.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor1StageConfig/multiply.out

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

# qsort
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig run-binary BINARY=${BMARKS}/qsort.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor1StageConfig/qsort.out

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

# rsort
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig run-binary BINARY=${BMARKS}/rsort.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor1StageConfig/rsort.out

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

# towers
cd ${LAB1ROOT}/sims/verilator
make CONFIG=Sodor1StageConfig run-binary BINARY=${BMARKS}/towers.riscv
${SCRIPTS}/tracer.py output/chipyard.TestHarness.Sodor1StageConfig/towers.out

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

### Vadd
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