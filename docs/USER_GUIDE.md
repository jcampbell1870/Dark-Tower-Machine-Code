# Dark Tower User Guide

This guide teaches how to use the Dark Tower Machine Code project, from first-time setup to assembly execution and simple high-level translation.

## What the project provides

The repository includes a lightweight machine environment inspired by IBM z/Architecture principles:

- instructions with registers and memory access
- jump, call, and return flow control
- simple arithmetic and loop behavior
- high-level translation support for educational scripts

## Running the project

From the repository root:

```bash
python3 src/dark_tower_assembler.py examples/hello.dt
python3 src/dark_tower_vm.py examples/hello.dt
python3 src/dark_tower_translator.py examples/factorial.dt
```

You may also use the translator with a custom input file, such as:

```text
SET x = 10
SET y = 5
SET total = x + y
PRINT total
HALT
```

## Basic assembly syntax

Dark Tower programs are written as a sequence of instructions and optional labels.

```text
MOV R1, 10
MOV R2, 5
ADD R1, R2
OUT R1
HALT
```

## Registers and memory

The VM uses the following register set:

- `R0` through `R7`

Memory is a fixed-size array of 4096 slots. Example:

```text
MOV R1, 125
STORE [100], R1
LOAD R2, [100]
OUT R2
HALT
```

## Control flow

Labels allow jumping to instructions and implementing loops.

```text
MOV R0, 0
start:
ADD R0, 1
OUT R0
JNZ R0, start
HALT
```

This example continues incrementing and printing until a stopping condition is reached.

## Comments

Use `;` or `#` to document source code.

```text
; Counter program
MOV R0, 0
ADD R0, 1
OUT R0
HALT
```

## Translator usage

The translator accepts a small high-level syntax:

```text
SET x = 10
SET y = 5
SET total = x + y
PRINT total
HALT
```

The tool emits assembly-like output that is easy to inspect and run.

## Best practices

- keep variables and labels readable
- use comments when a routine becomes longer
- test small programs before adding loops
- use `OUT` to debug values during development

## Summary

The Dark Tower environment is built to help you learn how a machine executes instructions, how control flow works, and how a translator can convert a simple language into machine-like operations.
