# Dark Tower Operating Manual

This manual describes how to use the Dark Tower environment as a teaching operating system and development sandbox.

## Purpose of the system

The Dark Tower project is a virtual operating environment for studying:

- registers and memory
- arithmetic and logic
- branch logic and loops
- machine execution
- translation from a higher-level language into assembly-like instructions

## System components

### 1. Virtual machine
The VM reads assembly instructions and executes them sequentially. It maintains the register file, memory array, and program counter.

### 2. Assembler
The assembler turns a source file into a human-readable machine code listing. It is ideal for learning how instructions are expressed in a structured machine format.

### 3. Translator
The translator accepts a minimalist high-level language and emits assembly-like statements.

## Running a program

From the repository root:

```bash
python3 src/dark_tower_vm.py examples/hello.dt
```

The output should appear in the terminal window.

## Creating your own programs

Create a new text file, for example:

```text
MOV R1, 9
MOV R2, 3
ADD R1, R2
OUT R1
HALT
```

Save the file as `examples/my_example.dt` and run:

```bash
python3 src/dark_tower_vm.py examples/my_example.dt
```

## Example programs

The repository includes:

- `examples/hello.dt` — basic arithmetic demo
- `examples/factorial.dt` — iterative multiplication example

## Troubleshooting

### Program does not start
- Check that the file path is correct.
- Verify that the file exists and is readable.
- Ensure instruction names are spelled correctly.

### Unexpected output
- Add `OUT` instructions before and after key operations.
- Check register values before branching.
- Confirm that jumps target valid labels.

### Halt issues
- Use `HALT` at the end of every program.
- Confirm branch logic does not create an infinite loop unless intentional.

## Security and teaching scope

This project is for education and experimentation only. It is not intended as production firmware or as a substitute for IBM system software.

## Summary

The Dark Tower operating environment is designed to be simple enough for novices to learn from while still showing good machine-system design ideas inspired by IBM mainframe architecture.
