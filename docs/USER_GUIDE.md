# Dark Tower User Guide

This guide explains how to use the Dark Tower OS with its advanced operating-system features, interpreter, process manager, and filesystem.

## Overview

The Dark Tower Operating System is a conceptual environment built to power Dark Tower-based computers and machine-code learning systems. It is inspired by IBM-like system architecture while remaining simple enough to study and modify.

The project now includes:

- a virtual machine
- an assembler
- a translator
- a language interpreter
- an operating-system runtime
- an interactive shell
- a filesystem abstraction
- a process manager
- a system monitor

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
registers
memory 32
ls
cat README.txt
processes
monitor
history
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

## Filesystem usage

The OS includes a simple filesystem abstraction that supports:

```text
ls
cat README.txt
write myfile.txt Hello Dark Tower
rm myfile.txt
```

## Process tracking

The process manager tracks active system processes and their execution state.

```text
processes
```

## Monitor view

The monitor gives a system-wide summary of the Dark Tower environment.

```text
monitor
```

## Programming recommendations

- keep programs small and readable
- validate memory and registers when debugging
- use `OUT` and `PRINT` for diagnostic values
- keep each process or routine focused on one operation
- end all programs with `HALT`

## Summary

The Dark Tower OS is intended to be a learning environment and conceptual operating platform for Dark Tower computer systems. It supports low-level execution, high-level interpretation, system monitoring, and general operating-system-style resource management in one repository.
