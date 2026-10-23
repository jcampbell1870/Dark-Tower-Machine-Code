# Dark Tower User Guide

This guide explains how to use the Dark Tower OS, the language interpreter, and the command shell in practice.

## Overview

The Dark Tower Operating System is a conceptual environment built to power Dark Tower-based computers and machine-code learning systems. It is inspired by IBM-style system architecture while remaining simple enough to study and modify.

The project includes:

- a virtual machine
- an assembler
- a translator
- a language interpreter
- an operating-system runtime
- an interactive shell

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
interpret examples/hello.dt
status
memory
quit
```

## Direct runtime execution

You may also execute a program directly without the shell:

```bash
python3 src/dark_tower_os.py examples/hello.dt
```

## Dark Tower interpreter

Run the interpreter directly:

```bash
python3 src/dark_tower_interpreter.py my_program.dt
```

Example interpreter source:

```text
SET total = 7
SET count = 5
SET result = total + count
PRINT result
HALT
```

## Assembly programs

```text
MOV R1, 7
MOV R2, 5
ADD R1, R2
OUT R1
HALT
```

## Shell responsibilities

The shell acts as the interface between a user and the Dark Tower kernel. It lets you:

- boot the system
- run machine programs
- interpret language scripts
- inspect machine state
- exit cleanly

## Programming recommendations

- keep programs small and readable
- use labels carefully
- use `OUT` or `PRINT` for debugging values
- make sure every routine halts cleanly
- build programs in stages instead of creating giant scripts at once

## Summary

The Dark Tower OS is intended to be a learning environment and a conceptual operating platform for Dark Tower computer systems. It supports low-level execution, high-level interpretation, and operator-friendly system interaction in one project.
