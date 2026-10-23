#!/usr/bin/env python3
"""Dark Tower assembler.

This module converts a readable Dark Tower assembly source file into a
machine-style listing. The listing is intentionally simple and educational,
not a full hardware binary encoding format.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

OPCODES = {
    "MOV": 0x01,
    "ADD": 0x02,
    "SUB": 0x03,
    "MUL": 0x04,
    "DIV": 0x05,
    "LOAD": 0x06,
    "STORE": 0x07,
    "JMP": 0x10,
    "JZ": 0x11,
    "JNZ": 0x12,
    "CALL": 0x13,
    "RET": 0x14,
    "OUT": 0x20,
    "IN": 0x21,
    "HALT": 0xFF,
}

COMMENT_PREFIXES = (";", "#")


def strip_comments(line: str) -> str:
    for marker in COMMENT_PREFIXES:
        if marker in line:
            line = line.split(marker, 1)[0]
    return line.strip()


def parse_operand(value: str):
    value = value.strip()
    if not value:
        return None
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if inner.startswith("R") and inner[1:].isdigit():
            return {"kind": "mem_reg", "value": int(inner[1:])}
        return {"kind": "mem", "value": int(inner)}
    if value.startswith("R") and value[1:].isdigit():
        return {"kind": "register", "value": int(value[1:])}
    if re.fullmatch(r"-?\d+", value):
        return {"kind": "immediate", "value": int(value)}
    return {"kind": "symbol", "value": value}


def parse_instruction(line: str):
    line = strip_comments(line)
    if not line:
        return None
    if line.endswith(":"):
        return {"label": line[:-1].strip(), "mnemonic": None, "args": []}

    match = re.match(r"([A-Z]+)\s*(.*)", line, re.IGNORECASE)
    if not match:
        raise ValueError(f"Unsupported instruction syntax: {line}")

    mnemonic = match.group(1).upper()
    rest = match.group(2).strip()
    args = []
    if rest:
        parts = [p.strip() for p in re.split(r"\s*,\s*|\s+", rest) if p.strip()]
        args = [parse_operand(part) for part in parts]

    if mnemonic not in OPCODES:
        raise ValueError(f"Unknown mnemonic: {mnemonic}")

    return {"label": None, "mnemonic": mnemonic, "args": args}


def parse_source(text: str):
    instructions: List[Dict] = []
    labels: Dict[str, int] = {}
    for line in text.splitlines():
        entry = parse_instruction(line)
        if entry is None:
            continue
        if entry["label"] is not None:
            labels[entry["label"]] = len(instructions)
            continue
        instructions.append({
            "mnemonic": entry["mnemonic"],
            "args": entry["args"],
            "line": line,
        })
    return instructions, labels


def resolve_labels(instructions, labels):
    resolved = []
    for instr in instructions:
        args = []
        for item in instr["args"]:
            if item and item.get("kind") == "symbol":
                args.append({"kind": "label", "value": item["value"], "resolved": labels.get(item["value"], 0)})
            else:
                args.append(item)
        resolved.append({"mnemonic": instr["mnemonic"], "args": args})
    return resolved


def encode_instruction(instr):
    mnemonic = instr["mnemonic"]
    opcode = OPCODES[mnemonic]
    encoded = [opcode]
    for item in instr["args"]:
        if item is None:
            continue
        kind = item.get("kind")
        if kind in {"immediate", "mem", "mem_reg"}:
            encoded.append(int(item["value"]) & 0xFF)
        elif kind in {"register"}:
            encoded.append(int(item["value"]) & 0xFF)
        elif kind == "label":
            encoded.append(int(item["resolved"]) & 0xFF)
        else:
            raise ValueError(f"Unsupported operand kind: {kind}")
    return encoded


def assemble_file(path: str):
    source = Path(path).read_text(encoding="utf-8")
    instructions, labels = parse_source(source)
    resolved = resolve_labels(instructions, labels)
    output_lines = []
    for index, instr in enumerate(resolved):
        machine = encode_instruction(instr)
        encoded_hex = " ".join(f"{value:02X}" for value in machine)
        output_lines.append(f"{index:04X}: {encoded_hex}  {instr['mnemonic']} {' '.join(_describe_operand(arg) for arg in instr['args'])}")
    return output_lines


def _describe_operand(arg):
    if arg is None:
        return ""
    kind = arg.get("kind")
    if kind == "immediate":
        return str(arg["value"])
    if kind == "register":
        return f"R{arg['value']}"
    if kind == "mem":
        return f"[{arg['value']}]"
    if kind == "mem_reg":
        return f"[R{arg['value']}]"
    if kind == "symbol":
        return arg["value"]
    if kind == "label":
        return str(arg["value"])
    return str(arg)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 dark_tower_assembler.py <source-file>")
        return 1

    input_path = Path(sys.argv[1])
    output_lines = assemble_file(str(input_path))
    for line in output_lines:
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
