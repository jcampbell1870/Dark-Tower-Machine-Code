# Dark Tower Machine Code Reference

This reference explains the Dark Tower virtual instruction set and its IBM z/Architecture-inspired design patterns.

## System model

The VM includes:

- eight general-purpose registers: `R0`..`R7`
- a 4096-slot memory array
- a program counter
- a stack for subroutine calls
- console I/O

## Instruction set summary

| Mnemonic | Opcode | Meaning |
| --- | ---: | --- |
| `MOV` | `0x01` | Move an immediate or register value into a destination register |
| `ADD` | `0x02` | Add source to destination |
| `SUB` | `0x03` | Subtract source from destination |
| `MUL` | `0x04` | Multiply destination by source |
| `DIV` | `0x05` | Divide destination by source |
| `LOAD` | `0x06` | Load a memory value into a register |
| `STORE` | `0x07` | Store a register value into memory |
| `JMP` | `0x10` | Jump to a label |
| `JZ` | `0x11` | Jump if a register equals zero |
| `JNZ` | `0x12` | Jump if a register is not zero |
| `CALL` | `0x13` | Call a label and push the return address |
| `RET` | `0x14` | Return from a subroutine |
| `OUT` | `0x20` | Print a value |
| `IN` | `0x21` | Read a value from input into a register |
| `HALT` | `0xFF` | Stop execution |

## Instruction semantics

### `MOV dst, src`
Copies a value into a register.

```text
MOV R1, 42
MOV R2, R1
```

### Arithmetic

```text
MOV R0, 10
ADD R0, 5
SUB R0, 2
MUL R0, 3
DIV R0, 2
OUT R0
```

### Memory access

```text
MOV R1, 99
STORE [100], R1
LOAD R2, [100]
OUT R2
```

### Branching

```text
MOV R0, 0
loop:
ADD R0, 1
JNZ R0, loop
HALT
```

### Calls and returns

```text
CALL subroutine
RET

subroutine:
MOV R0, 7
OUT R0
RET
```

## Design notes

This instruction set is intentionally small and readable. It is built for teaching, not for emulating all IBM hardware intricacies. The result is a compact, understandable system that follows the same architectural patterns used in IBM mainframe environments: explicit register operations, memory addressing, branch control, and machine-level execution order.
