# Dark Tower User Guide

This guide explains how to use the Dark Tower OS, the language processor, the runtime, and the interactive shell.

## Overview

The Dark Tower Operating System is a conceptual environment built to power Dark Tower-based computers. It is rooted in IBM-inspired machine principles, but implemented as an educational and portable simulator.

The project includes:

- a virtual machine
- an assembler
- a translator and source processor
- an operating-system-style runtime
- a command shell

## Starting the system

Launch the shell from the repository root:

```bash
python3 src/dark_tower_shell.py
```

Example shell commands:

```text
help
boot
run examples/hello.dt
status
memory
quit
```

## Direct runtime execution

You may also execute a program directly without the shell:

```bash
python3 src/dark_tower_os.py examples/hello.dt
```

## Example programs

The repository contains:

- `examples/hello.dt` — startup and output demonstration
- `examples/factorial.dt` — loop-based arithmetic example

## Assembly programs

An assembly program can look like this:

```text
MOV R1, 7
MOV R2, 5
ADD R1, R2
OUT R1
HALT
```

The runtime reads this sequence and executes it with the machine model.

## High-level source

The language processor can accept a more readable form:

```text
SET total = 7
SET count = 5
SET result = total + count
PRINT result
HALT
```

It translates the source into assembly-like instructions that the runtime can interpret.

## Shell responsibilities

The shell is the user interface for the Dark Tower OS. It allows you to:

- boot the system
- launch programs
- check machine status
- inspect memory
- exit cleanly

## Programming recommendations

- keep programs small and readable
- use labels carefully
- use `OUT` to debug intermediate values
- make sure each program ends with `HALT`
- develop in small steps rather than large monolithic blocks

## Summary

The Dark Tower OS is meant to be a learning environment and a conceptual operating platform for Dark Tower computer systems. It is designed to help users understand machine execution, translation, and user-facing operating logic in one place.
