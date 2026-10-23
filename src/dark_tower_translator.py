#!/usr/bin/env python3
"""Dark Tower translator.

This utility converts a tiny high-level language into Dark Tower assembly.
It is intentionally small and designed for educational use.
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


def expression_to_value(expr: str, variables: dict):
    cleaned = expr.strip()
    if cleaned in variables:
        return variables[cleaned]
    if re.fullmatch(r"-?\d+", cleaned):
        return int(cleaned)
    code = compile(cleaned, "<dt>", "eval")
    safe_env = {}
    for key, value in variables.items():
        safe_env[key] = value
    return eval(code, {"__builtins__": {}}, safe_env)


def translate_lines(lines):
    variables = {}
    output = []
    reg_counter = 0

    for raw in lines:
        line = raw.strip()
        if not line or line.startswith(";") or line.startswith("#"):
            continue

        if line.upper().startswith("HALT"):
            output.append("HALT")
            continue

        if line.upper().startswith("PRINT "):
            target = line[6:].strip()
            output.append(f"OUT {target if target.startswith('R') or target.isdigit() or target.startswith('-') else variables[target]}")
            continue

        match = re.match(r"SET\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+)", line)
        if match:
            name, expr = match.groups()
            value = expression_to_value(expr, variables)
            reg = f"R{reg_counter % 8}"
            output.append(f"MOV {reg}, {value}")
            variables[name] = reg
            reg_counter += 1
            continue

        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", line):
            if line in variables:
                output.append(f"OUT {variables[line]}")
            continue

        raise ValueError(f"Unsupported translation input: {line}")

    return output


def translate_file(path: str):
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()
    return translate_lines(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 dark_tower_translator.py <source-file>")
        return 1

    source = Path(sys.argv[1])
    try:
        translated = translate_file(str(source))
    except Exception as exc:
        print(f"Translation error: {exc}")
        return 1

    for line in translated:
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
