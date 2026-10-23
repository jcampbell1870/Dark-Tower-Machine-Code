# Dark Tower User Guide

This guide explains how the Dark Tower Operating System and its language processing tools are used in practice.

## Overview

The Dark Tower Operating System is a virtual, IBM-inspired operating environment designed to run machine-code programs, educational operating-system patterns, and a translated high-level language pipeline.

It is built to support:

- machine-level execution
- assembly programming
- instruction translation
- educational OS concepts
- platform design for Dark Tower-based computers

## Core components

- `src/dark_tower_vm.py` — the machine runtime
- `src/dark_tower_assembler.py` — converts assembly to machine-style output
- `src/dark_tower_translator.py` — translates simple source into assembly
- `src/dark_tower_language_processor.py` — higher-level language processing front end
- `src/dark_tower_os.py` — OS-style boot/runtime environment

## Running the Dark Tower OS

From the repository root:

```bash
python3 src/dark_tower_os.py examples/hello.dt
```

This boots the virtual OS runtime and executes the program in the same way a small system would load and run a user program.

## Language processing

Use the language processor on source text like:

```text
SET total = 7
SET count = 5
SET result = total + count
PRINT result
HALT
```

Run:

```bash
python3 src/dark_tower_language_processor.py my_program.dt
```

The output is assembly-like instructions that can be interpreted by the runtime.

## Memory and registers

The OS uses:

- `R0` to `R7` as general-purpose registers
- a 4096-cell memory array
- a call stack for subroutines
- a program counter for sequential execution

## Development workflow

1. Write a high-level or assembly program.
2. Run the language processor or assembler.
3. Load the resulting instructions into the Dark Tower VM or OS runtime.
4. Observe output and refine the logic.

## Recommended patterns

- Use comments to explain code paths.
- Keep labels unique.
- Use `OUT` for debugging intermediate values.
- End every program with `HALT`.
- Test small programs before scaling to longer routines.

## Dark Tower OS philosophy

The Dark Tower operating system is intended to act as a conceptual, educational platform for machine-code computing. It is meant to teach how machines boot, execute instructions, manage memory, and translate higher-level source into operating-system-acceptable logic.
