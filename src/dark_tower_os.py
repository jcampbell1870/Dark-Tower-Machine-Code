#!/usr/bin/env python3
"""Dark Tower OS runtime.

This module provides a lightweight operating-system-style runtime for the Dark
Tower machine environment. It manages the boot and execution loop, memory,
registers, and program flow in a way that feels similar to a small system
kernel or monitor.
"""

from __future__ import annotations

import sys
from pathlib import Path

from dark_tower_assembler import parse_source, resolve_labels


class DarkTowerOS:
    def __init__(self):
        self.registers = {f"R{i}": 0 for i in range(8)}
        self.memory = [0] * 4096
        self.stack = []
        self.labels = {}
        self.instructions = []

    def load_program(self, path: str):
        source = Path(path).read_text(encoding="utf-8")
        self.instructions, self.labels = parse_source(source)
        self.instructions = resolve_labels(self.instructions, self.labels)
        return self.instructions

    def get_operand_value(self, operand):
        if operand is None:
            return 0
        kind = operand.get("kind")
        if kind == "register":
            return self.registers.get(f"R{operand['value']}", 0)
        if kind == "immediate":
            return operand["value"]
        if kind == "label":
            return operand["resolved"]
        if kind == "symbol":
            return operand["value"]
        return 0

    def set_register(self, index: int, value):
        self.registers[f"R{index}"] = int(value)

    def execute(self, path: str):
        self.load_program(path)
        pc = 0

        while pc < len(self.instructions):
            instr = self.instructions[pc]
            mnemonic = instr["mnemonic"]
            args = instr["args"]

            if mnemonic == "MOV":
                dest, source = args[0], args[1]
                if dest.get("kind") == "register":
                    self.registers[f"R{dest['value']}"] = self.get_operand_value(source)
                pc += 1
                continue

            if mnemonic == "ADD":
                dest, source = args[0], args[1]
                self.registers[f"R{dest['value']}"] += self.get_operand_value(source)
                pc += 1
                continue

            if mnemonic == "SUB":
                dest, source = args[0], args[1]
                self.registers[f"R{dest['value']}"] -= self.get_operand_value(source)
                pc += 1
                continue

            if mnemonic == "MUL":
                dest, source = args[0], args[1]
                self.registers[f"R{dest['value']}"] *= self.get_operand_value(source)
                pc += 1
                continue

            if mnemonic == "DIV":
                dest, source = args[0], args[1]
                divisor = self.get_operand_value(source)
                if divisor == 0:
                    raise ZeroDivisionError("Dark Tower OS: division by zero")
                self.registers[f"R{dest['value']}"] //= divisor
                pc += 1
                continue

            if mnemonic == "LOAD":
                dest, location = args[0], args[1]
                if location.get("kind") == "mem":
                    self.registers[f"R{dest['value']}"] = self.memory[location["value"]]
                elif location.get("kind") == "mem_reg":
                    self.registers[f"R{dest['value']}"] = self.memory[self.registers[f"R{location['value']}"]]
                pc += 1
                continue

            if mnemonic == "STORE":
                location, source = args[0], args[1]
                value = self.get_operand_value(source)
                if location.get("kind") == "mem":
                    self.memory[location["value"]] = value
                elif location.get("kind") == "mem_reg":
                    self.memory[self.registers[f"R{location['value']}"]] = value
                pc += 1
                continue

            if mnemonic == "JMP":
                target = args[0]["value"]
                pc = self.labels.get(target, pc)
                continue

            if mnemonic == "JZ":
                reg, target = args[0], args[1]
                if self.registers[f"R{reg['value']}"] == 0:
                    pc = self.labels.get(target["value"], pc)
                else:
                    pc += 1
                continue

            if mnemonic == "JNZ":
                reg, target = args[0], args[1]
                if self.registers[f"R{reg['value']}"] != 0:
                    pc = self.labels.get(target["value"], pc)
                else:
                    pc += 1
                continue

            if mnemonic == "CALL":
                target = args[0]["value"]
                self.stack.append(pc + 1)
                pc = self.labels.get(target, pc)
                continue

            if mnemonic == "RET":
                pc = self.stack.pop() if self.stack else len(self.instructions)
                continue

            if mnemonic == "OUT":
                print(self.get_operand_value(args[0]))
                pc += 1
                continue

            if mnemonic == "IN":
                reg = args[0]["value"]
                self.registers[f"R{reg}"] = int(input("Dark Tower OS input> "))
                pc += 1
                continue

            if mnemonic == "HALT":
                break

            raise ValueError(f"Unsupported instruction: {mnemonic}")

        return self.registers, self.memory


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 dark_tower_os.py <program-file>")
        return 1

    program_path = Path(sys.argv[1])
    if not program_path.exists():
        print(f"Program not found: {program_path}")
        return 1

    try:
        os_runtime = DarkTowerOS()
        os_runtime.execute(str(program_path))
        print("Dark Tower OS runtime completed successfully.")
    except Exception as exc:
        print(f"Dark Tower OS error: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
