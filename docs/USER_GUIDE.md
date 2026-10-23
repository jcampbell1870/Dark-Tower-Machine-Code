# Dark Tower User Guide

This guide explains how to use the Dark Tower OS with its advanced operating-system features, interpreter, process manager, filesystem, scheduler, bootloader, and system-call interface.

## Overview

The Dark Tower Operating System is a conceptual environment built to power Dark Tower-based computers and machine-code learning systems. It is inspired by IBM-like system architecture while remaining simple enough to study and modify.

The project includes:

- a virtual machine
- an assembler
- a translator
- a language interpreter
- an operating-system runtime
- an interactive shell
- a filesystem abstraction
- a process manager
- a scheduler
- a bootloader
- a system-call interface
- a console session manager

## Starting the system

Launch the shell from the repository root:

```bash
python3 src/dark_tower_shell.py
```

Example shell commands:

```text
help
boot
bootloader
run examples/hello.dt
interpret examples/hello.dt
status
registers
memory 32
ls
cat README.txt
processes
scheduler
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

## Process and scheduler usage

The process manager tracks active system processes and their execution state, while the scheduler manages a simple ready queue.

```text
processes
scheduler
```

## System calls

The system call interface supports commands such as:

```text
read README.txt
status
memdump 16
run examples/hello.dt
help
```

## Console and boot workflow

Use the bootloader or shell to initialize the system and then interact with the console session.

```text
bootloader
```

## Summary

The Dark Tower OS is intended to be a learning environment and conceptual operating platform for Dark Tower computer systems. It supports low-level execution, high-level interpretation, system monitoring, resource management, and system-call behavior in one repository.
