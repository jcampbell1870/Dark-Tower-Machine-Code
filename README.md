# Dark Tower Operating System

The Dark Tower Operating System is a conceptual IBM-inspired operating environment designed to power Dark Tower-based computers, machine-code training systems, and educational platforms for low-level software design.

This project is intended to function as a small operating system and programming environment with:

- a boot sequence
- a kernel-style runtime layer
- program execution under a system monitor
- memory and register management
- a low-level machine model
- a high-level language interpreter
- a command shell for system control and program launch

## Project overview

The repository includes:

- `src/dark_tower_vm.py` — the Dark Tower virtual machine runtime
- `src/dark_tower_assembler.py` — converts assembly to machine-style output
- `src/dark_tower_translator.py` — simple translation utility for readable source
- `src/dark_tower_os.py` — operating-system-style runtime
- `src/dark_tower_kernel.py` — kernel-level runtime and system control
- `src/dark_tower_shell.py` — Dark Tower interactive shell
- `src/dark_tower_interpreter.py` — full interpreter for the Dark Tower programming language
- `src/dark_tower_language_processor.py` — language processing front end
- `examples/hello.dt` — startup and output example
- `examples/factorial.dt` — arithmetic loop example
- `docs/USER_GUIDE.md` — beginner operational guide
- `docs/MACHINE_CODE_REFERENCE.md` — instruction set and machine model
- `docs/OPERATING_MANUAL.md` — operation and maintenance guide
- `docs/OS_ARCHITECTURE.md` — system architecture overview
- `docs/INTERPRETER_GUIDE.md` — Dark Tower interpreter reference

## Why this system matters

The Dark Tower OS is inspired by IBM mainframe principles:

- explicit register usage
- memory addressing
- structured execution flow
- stack-oriented control patterns
- machine-language translation from readable source
- operating-system control and monitoring

## Quick start

Launch the interactive shell:

```bash
python3 src/dark_tower_shell.py
```

Supported shell commands:

```text
boot
run examples/hello.dt
interpret examples/hello.dt
status
memory
help
quit
```

You can also run the OS runtime directly:

```bash
python3 src/dark_tower_os.py examples/hello.dt
```

## Sample assembly program

```text
MOV R1, 7
MOV R2, 5
ADD R1, R2
OUT R1
HALT
```

## Sample interpreter source

```text
SET total = 7
SET count = 5
SET result = total + count
PRINT result
HALT
```

The interpreter executes this source directly rather than only translating it.

## Dark Tower interpreter

The interpreter is a full computer-programming language runtime for the Dark Tower environment. It supports:

- variable assignment
- arithmetic expressions
- print operations
- conditionals
- loops
- labels and jumps
- halting the program

Run it directly with:

```bash
python3 src/dark_tower_interpreter.py examples/hello.dt
```

This interprets Dark Tower source code and executes the logic in a human-readable language.

## Operating-system features

The Dark Tower OS includes:

- boot sequence and banner output
- kernel-style runtime shell
- system status and memory introspection
- command-driven OS control
- programs loaded and executed from files
- a conceptual architecture suitable for Dark Tower computer systems

## Learning path

1. Start the shell and run `boot`.
2. Run the example programs in `examples/`.
3. Read `docs/OS_ARCHITECTURE.md`.
4. Study the machine reference.
5. Write your own Dark Tower programs and run them through the interpreter.

## License

This project is distributed under the MIT License.
