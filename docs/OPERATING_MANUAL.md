# Dark Tower Operating Manual

This manual documents the operational use of the Dark Tower Operating System and explains how the system is intended to power Dark Tower-based computers.

## System purpose

The Dark Tower OS is designed to support:

- machine-code execution
- permit low-level programming tasks
- provide system-level execution behavior
- act as a teaching environment for IBM-inspired system design
- allow high-level source to be translated into machine-executable instructions

## Boot process

The runtime boots the machine environment and initializes memory, registers, and the execution layer. The boot sequence is implemented conceptually through the kernel and shell.

```bash
python3 src/dark_tower_shell.py
```

This launches the shell, where users may run commands such as:

```text
boot
run examples/hello.dt
status
memory
help
quit
```

## Runtime and interpreter behavior

The system step is as follows:

1. the program is loaded
2. instructions are parsed
3. labels are resolved
4. memory and registers are initialized
5. execution begins at the first instruction
6. results are printed or returned
7. the system halts gracefully or reports an error

## Example execution flow

```bash
python3 src/dark_tower_os.py examples/hello.dt
```

This is the direct execution pathway for a Dark Tower program.

## Memory model

The OS uses a 4096-slot memory array and a register set from `R0` through `R7`. Memory usage is simple and deterministic so it is easy to teach and debug.

## Shell operations

The shell provides the user-oriented command layer for the Dark Tower OS. It acts as the front-end between the human operator and the operating system kernel.

Recommended operations:

- `boot` to initialize the environment
- `run` to execute a source or program file
- `status` to inspect current machine state
- `memory` to view early memory cells
- `help` to review commands

## Troubleshooting

### Program errors
- confirm the file path exists
- verify instruction spelling
- ensure labels are resolved properly
- check for division by zero or invalid memory access

### Shell issues
- ensure the repository root is correct
- use `python3` to run the shell
- open the file from the correct directory path

## Summary

The Dark Tower Operating System is intended to provide a clear, educational, and extensible operating platform for Dark Tower-based computing. It supports machine execution, boot and runtime behavior, source translation, and a system shell to help operators and programmers learn how a real machine environment behaves.
