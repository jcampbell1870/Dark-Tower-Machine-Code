# Dark Tower Machine Code

Dark Tower Machine Code is a compact, IBM z/Architecture-inspired virtual machine environment designed to teach machine execution, instruction encoding, memory addressing, and operating-system-like control flow in a simple Python implementation.

The project includes:

- a virtual machine runtime for the Dark Tower instruction set
- an assembler for turning source code into machine-readable listings
- a translator from a small high-level language into assembly
- example programs and training manuals
- educational documentation for learning and experimentation

This repository is intentionally readable and portable. It is not a clone of IBM proprietary hardware or firmware; it is a clean educational implementation inspired by IBM mainframe architecture principles.

## Repository layout

- `src/dark_tower_vm.py` — executes Dark Tower assembly programs
- `src/dark_tower_assembler.py` — assembles source into a machine-code style listing
- `src/dark_tower_translator.py` — translates simple high-level statements to assembly
- `examples/hello.dt` — basic arithmetic and output example
- `examples/factorial.dt` — loop-based factorial example
- `docs/USER_GUIDE.md` — beginner-friendly user manual
- `docs/MACHINE_CODE_REFERENCE.md` — machine architecture reference
- `docs/OPERATING_MANUAL.md` — system operations guide

## Quick start

From the repository root:

```bash
python3 src/dark_tower_assembler.py examples/hello.dt
python3 src/dark_tower_vm.py examples/hello.dt
python3 src/dark_tower_translator.py examples/factorial.dt
```

## Example assembly

```text
MOV R1, 7
MOV R2, 5
ADD R1, R2
OUT R1
HALT
```

This program loads values into registers, adds them, prints the result, and halts.

## The Dark Tower machine model

The runtime uses:

- general-purpose registers: `R0` to `R7`
- a memory array with 4096 slots
- a program counter
- a stack for subroutine calls
- console input/output

## Learning path

1. Read `docs/USER_GUIDE.md`
2. Study `docs/MACHINE_CODE_REFERENCE.md`
3. Run the examples in `examples/`
4. Modify programs and test new control flow
5. Translate your own high-level scripts into Dark Tower assembly

## License

This project is distributed under the MIT License.
