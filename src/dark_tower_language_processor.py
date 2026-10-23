#!/usr/bin/env python3
"""Dark Tower language processor and translator.

This module behaves as a compiler-style front-end for the Dark Tower OS.
It accepts high-level commands and converts them into assembly-like machine
instructions for the Dark Tower VM.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


class DarkTowerLanguageProcessor:
    def __init__(self):
        self.variables = {}
        self.register_counter = 0
        self.output = []

    def translate_expression(self, expr: str):
        expr = expr.strip()
        if expr in self.variables:
            return self.variables[expr]
        if re.fullmatch(r"-?\d+", expr):
            return int(expr)
        try:
            value = int(expr)
        except ValueError:
            value = expr
        return value

    def parse_line(self, line: str):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith(";"):
            return None

        if line.upper().startswith("HALT"):
            self.output.append("HALT")
            return

        if line.upper().startswith("PRINT "):
            value = line[6:].strip()
            targ = self.translate_expression(value)
            self.output.append(f"OUT {targ}")
            return

        match = re.match(r"SET\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+)", line)
        if match:
            name, expr = match.groups()
            reg = f"R{self.register_counter % 8}"
            value = self.translate_expression(expr)
            self.output.append(f"MOV {reg}, {value}")
            self.variables[name] = reg
            self.register_counter += 1
            return

        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", line):
            if line in self.variables:
                self.output.append(f"OUT {self.variables[line]}")
            return

        raise ValueError(f"Unsupported language statement: {line}")

    def process(self, source_text: str):
        for raw_line in source_text.splitlines():
            self.parse_line(raw_line)
        return self.output


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 dark_tower_language_processor.py <source-file>")
        return 1

    source_path = Path(sys.argv[1])
    if not source_path.exists():
        print(f"File not found: {source_path}")
        return 1

    try:
        processor = DarkTowerLanguageProcessor()
        source = source_path.read_text(encoding="utf-8")
        translated = processor.process(source)
    except Exception as exc:
        print(f"Dark Tower language processing error: {exc}")
        return 1

    for line in translated:
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
