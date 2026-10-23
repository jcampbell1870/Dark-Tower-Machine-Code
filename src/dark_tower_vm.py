#!/usr/bin/env python3
"""Dark Tower virtual machine.

The runtime executes assembly programs in the Dark Tower instruction set.
It is intentionally simple, portable, and educational.
"""

from __future__ import annotations

import sys
from pathlib import Path

from dark_tower_assembler import parse_source, resolve_labels

REGISTERS = {f"R{i}": 0 for i in range(8)}


def load_program(path: str):
    source = Path(path).read_text(encoding="utf-8")
    instructions, labels = parse_source(source)
    return resolve_labels(instructions, labels), labels


def get_register_value(registers, operand):
    if operand is None:
        return 0
    kind = operand.get("kind")
    if kind == "register":
        return registers.get(f"R{operand['value']}", 0)
    if kind == "immediate":
        return operand["value"]
    if kind == "label":
        return operand["resolved"]
    if kind == "symbol":
        return operand["value"]
    return 0


def set_register(registers, index, value):
    registers[f"R{index}"] = int(value)


def resolve_memory_operand(memory, operand):
    if operand is None:
        return 0
    kind = operand.get("kind")
    if kind == "mem":
        return memory[operand["value"]]
    if kind == "mem_reg":
        return memory[registers[f"R{operand['value']}"]]
    return get_register_value(registers, operand)


def execute_program(path: str):
    instructions, labels = load_program(path)
    registers = {f"R{i}": 0 for i in range(8)}
    memory = [0] * 4096
    stack = []
    pc = 0

    while pc < len(instructions):
        instr = instructions[pc]
        mnemonic = instr["mnemonic"]
        args = instr["args"]

        if mnemonic == "MOV":
            dest = args[0]
            source = args[1]
            if dest.get("kind") == "register":
                registers[f"R{dest['value']}"] = get_register_value(registers, source)
            pc += 1
            continue

        if mnemonic == "ADD":
            dest = args[0]
            source = args[1]
            value = get_register_value(registers, source)
            reg_index = dest["value"]
            registers[f"R{reg_index}"] += value
            pc += 1
            continue

        if mnemonic == "SUB":
            dest = args[0]
            source = args[1]
            value = get_register_value(registers, source)
            reg_index = dest["value"]
            registers[f"R{reg_index}"] -= value
            pc += 1
            continue

        if mnemonic == "MUL":
            dest = args[0]
            source = args[1]
            value = get_register_value(registers, source)
            reg_index = dest["value"]
            registers[f"R{reg_index}"] *= value
            pc += 1
            continue

        if mnemonic == "DIV":
            dest = args[0]
            source = args[1]
            value = get_register_value(registers, source)
            reg_index = dest["value"]
            if value == 0:
                raise ZeroDivisionError("Division by zero in Dark Tower program")
            registers[f"R{reg_index}"] //= value
            pc += 1
            continue

        if mnemonic == "LOAD":
            dest = args[0]
            location = args[1]
            reg_index = dest["value"]
            if location.get("kind") == "mem":
                registers[f"R{reg_index}"] = memory[location["value"]]
            elif location.get("kind") == "mem_reg":
                registers[f"R{reg_index}"] = memory[registers[f"R{location['value']}"]]
            pc += 1
            continue

        if mnemonic == "STORE":
            location = args[0]
            source = args[1]
            value = get_register_value(registers, source)
            if location.get("kind") == "mem":
                memory[location["value"]] = value
            elif location.get("kind") == "mem_reg":
                memory[registers[f"R{location['value']}"]] = value
            pc += 1
            continue

        if mnemonic == "JMP":
            pc = labels.get(args[0]["value"], pc)
            continue

        if mnemonic == "JZ":
            reg = args[0]
            target = args[1]
            if registers[f"R{reg['value']}"] == 0:
                pc = labels.get(target["value"], pc)
            else:
                pc += 1
            continue

        if mnemonic == "JNZ":
            reg = args[0]
            target = args[1]
            if registers[f"R{reg['value']}"] != 0:
                pc = labels.get(target["value"], pc)
            else:
                pc += 1
            continue

        if mnemonic == "CALL":
            target = args[0]
            stack.append(pc + 1)
            pc = labels.get(target["value"], pc)
            continue

        if mnemonic == "RET":
            pc = stack.pop() if stack else len(instructions)
            continue

        if mnemonic == "OUT":
            value = get_register_value(registers, args[0])
            print(value)
            pc += 1
            continue

        if mnemonic == "IN":
            reg_index = args[0]["value"]
            value = int(input("Dark Tower input> "))
            registers[f"R{reg_index}"] = value
            pc += 1
            continue

        if mnemonic == "HALT":
            break

        raise ValueError(f"Unsupported mnemonic: {mnemonic}")

    return registers, memory


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 dark_tower_vm.py <program-file>")
        return 1

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Program not found: {path}")
        return 1

    try:
        execute_program(str(path))
    except Exception as exc:  # pragma: no cover - runtime reporting
        print(f"Dark Tower VM error: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
