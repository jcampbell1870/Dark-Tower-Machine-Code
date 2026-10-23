# Dark Tower Operating System

The Dark Tower Operating System is an IBM-inspired virtual operating environment designed to power computers, training systems, and machine-code experiments built around the Dark Tower machine architecture.

This repository is not a copy of IBM proprietary product code. It is a clean, educational, and extensible operating-system platform inspired by IBM mainframe design principles: explicit register usage, memory management, branch logic, execution flow, and machine-language translation.

## What is included

- `src/dark_tower_vm.py` — the Dark Tower virtual machine that executes machine programs
- `src/dark_tower_assembler.py` — assembler that converts assembly to machine-style output
- `src/dark_tower_translator.py` — translator from a simple high-level language to assembly
- `src/dark_tower_language_processor.py` — a language processor and translation frontend
- `src/dark_tower_os.py` — the operating-system-style runtime and boot environment
- `examples/hello.dt` — a basic system startup and output example
- `examples/factorial.dt` — arithmetic loop example
- `docs/USER_GUIDE.md` — practical operating guide
- `docs/MACHINE_CODE_REFERENCE.md` — instruction set and machine model reference
- `docs/OPERATING_MANUAL.md` — system operations and maintenance guide

## Design goals

This project is designed to power Dark Tower-based computers with:

- a bootable-style operating runtime
- deterministic instruction execution
- general-purpose registers and memory model
- machine-code translation from a readable programming language
- support for teaching, experimentation, and system design

## Quick start

From the repository root:

```bash
python3 src/dark_tower_assembler.py examples/hello.dt
python3 src/dark_tower_vm.py examples/hello.dt
python3 src/dark_tower_language_processor.py examples/hello.dt
python3 src/dark_tower_os.py examples/hello.dt
```

## Dark Tower OS execution model

The Dark Tower OS run environment includes:

- register file: `R0` through `R7`
- memory array: 4096 cells
- program counter: instruction address tracker
- stack: subroutine and procedure support
- console I/O: print and read operations
- boot and run loop: loads a program and executes it in a stable runtime

## Sample Dark Tower assembly

```text
MOV R1, 7
MOV R2, 5
ADD R1, R2
OUT R1
HALT
```

This instruction sequence loads values, adds them, prints the result, and halts the machine. It is the basic form of a Dark Tower computer program.

## Language processor and translator

The project includes a high-level translator that turns simple statements into assembly-like instructions. The language processing model helps students and developers move from readable source code to executable machine logic.

Example high-level source:

```text
SET total = 7
SET count = 5
SET result = total + count
PRINT result
HALT
```

The translation layer converts these statements into instructions understood by the Dark Tower VM.

## Learning path

1. Read the user guide.
2. Study the machine-code reference.
3. Run the example programs.
4. Edit the examples and experiment with new instructions.
5. Build custom programs that operate inside the Dark Tower OS runtime.

## Operating-system philosophy

The Dark Tower OS is a conceptual operating system for educational and experimental computing. It emphasizes:

- ownership of resources and memory
- stable program flow
- readable instruction design
- process-like execution segments
- compatibility with modern training workflows

## License

This project is distributed under the MIT License.
