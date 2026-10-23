# Dark Tower Operating System Architecture

This document describes the architecture of the Dark Tower Operating System and how it is intended to power Dark Tower-based computers.

## 1. Overview

The Dark Tower OS is a conceptual operating environment built for educational and experimental software systems. It combines machine-code execution, memory handling, operating-style control flow, and a translator for high-level instruction sources.

The goal is to provide a realistic enough environment to teach how an operating system interacts with machine resources while remaining accessible to beginners.

## 2. Core system components

### Kernel
The kernel is the system control layer. It manages bootstrapping, status, memory views, and execution requests.

### Machine runtime
The machine runtime provides the lower-level execution model for instructions, including registers, memory, stack management, and the program counter.

### Translator and language processor
The translator converts a simplified high-level source language into assembly-like instructions that the machine can execute. This allows users to program in a more readable syntax while preserving a machine-centric execution model.

### Shell interface
The shell provides user interaction and a command-style interface for running programs, checking status, and booting the environment.

## 3. Execution model

The Dark Tower OS moves through the following lifecycle:

1. boot the system
2. initialize memory and registers
3. load a program
4. parse and resolve instructions
5. execute code in the runtime
6. report results or errors
7. return to shell control or terminate

## 4. Memory and register architecture

The system uses:

- eight general-purpose integer registers: `R0` to `R7`
- a 4096-cell memory array
- a program counter to track the active instruction
- a stack for subroutine and call flow
- a console for input and output

This model is intentionally simple but faithful to the principles behind many IBM-inspired systems.

## 5. Command model

The shell supports commands such as:

- `boot` — initialize the machine and optionally launch a program
- `run` — execute a Dark Tower source file
- `status` — display current registers
- `memory` — inspect early memory cells
- `help` — show available commands
- `quit` — exit the shell

## 6. Programming model

Dark Tower programs may be written directly in machine code or translated from a simple high-level language. The system supports both, which makes it suitable for learning different layers of system design.

## 7. Intended use

The Dark Tower OS is intended for:

- education
- low-level programming exploration
- system design teaching
- experimentation with instruction-set design
- understanding how machine execution relates to operating-system control

## 8. Future growth

This architecture can be extended by adding:

- a file system abstraction
- scheduler support
- process tracking
- user-space task management
- richer instruction sets
- bootloader support for multi-program environments

## Summary

The Dark Tower OS is a conceptual operating environment designed to power Dark Tower-based computers while also serving as a readable and teachable representation of machine-level and system-level execution.
