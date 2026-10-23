# Dark Tower Operating System

The Dark Tower Operating System is a conceptual IBM-inspired operating environment designed to power Dark Tower-based computers, machine-code training systems, and educational platforms for low-level software design.

This project is meant to be more than a toy machine emulator. It is designed to behave like a small operating system environment with:

- a boot sequence
- a kernel-style runtime layer
- program execution under a system monitor
- memory and register management
- a language and translation layer for assembly and simple high-level programs
- a command shell for system control and program launch

## Project overview

The repository includes:

- `src/dark_tower_vm.py` — virtual machine runtime
- `src/dark_tower_assembler.py` — assembly-to-machine listing utility
- `src/dark_tower_translator.py` — simple translator from readable source to assembly output
- `src/dark_tower_os.py` — operating-system-style runtime
- `src/dark_tower_kernel.py` — kernel-level runtime and system control layer
- `src/dark_tower_shell.py` — interactive Dark Tower system shell
- `src/dark_tower_language_processor.py` — high-level source processing front end
- `examples/hello.dt` — boot and output example
- `examples/factorial.dt` — arithmetic loop example
- `docs/USER_GUIDE.md` — operator and programmer guide
- `docs/MACHINE_CODE_REFERENCE.md` — machine architecture reference
- `docs/OPERATING_MANUAL.md` — operating-system operations guide
- `docs/OS_ARCHITECTURE.md` — architectural overview of the Dark Tower OS

## Why this system matters

The Dark Tower OS is intentionally inspired by IBM mainframe architecture principles:

- explicit register usage
- memory addressing
- structured execution flow
- queue-like or stack-based control patterns
- machine-language translation from readable source
- system-level boot and runtime management

This makes it suitable for education, simulation, and experimentation in machine-language operating systems.

## Quick start

Launch the interactive shell:

```bash
python3 src/dark_tower_shell.py
```

Then use commands such as:

```text
boot
run examples/hello.dt
status
memory
help
quit
```

You can also run the OS runtime directly:

```bash
python3 src/dark_tower_os.py examples/hello.dt
```

## Sample Dark Tower instructions

```text
MOV R1, 7
MOV R2, 5
ADD R1, R2
OUT R1
HALT
```

This is the basic machine-code pattern used by Dark Tower programs: load values into registers, perform arithmetic, output the result, and halt.

## High-level language entry

The language processor lets users write easier source and translate it into system-friendly instructions.

Example source:

```text
SET total = 7
SET count = 5
SET result = total + count
PRINT result
HALT
```

The front-end converts this into machine-like assembly instructions for the runtime.

## Operating-system features

The Dark Tower OS now includes:

- boot sequence and banner output
- kernel-style runtime shell
- system status and memory introspection
- command-driven OS control
- program loading and execution management
- a conceptual architecture suitable for Dark Tower computer systems

## Learning path

1. Start the shell and run `boot`.
2. Run the example programs in `examples/`.
3. Read `docs/OS_ARCHITECTURE.md`.
4. Study the machine reference.
5. Write your own Dark Tower programs and test them in the shell.

## License

This project is distributed under the MIT License.
