#!/usr/bin/env python3
"""Dark Tower interpreter.

This interpreter executes a small, computer-programming language designed for
Dark Tower operating-system programs. It directly evaluates statements such as
SET, PRINT, IF, WHILE, LABEL, GOTO, and HALT.
"""

from __future__ import annotations

import ast
import math
import operator
import re
import sys
from pathlib import Path
from typing import Any, Dict, List


ALLOWED_BINOPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
}

ALLOWED_BOOLOPS = {
    ast.And: lambda a, b: a and b,
    ast.Or: lambda a, b: a or b,
}

ALLOWED_CMPOPS = {
    ast.Eq: operator.eq,
    ast.NotEq: operator.ne,
    ast.Gt: operator.gt,
    ast.GtE: operator.ge,
    ast.Lt: operator.lt,
    ast.LtE: operator.le,
}

ALLOWED_UNARYOPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
    ast.Not: operator.not_,
}

MAX_LOOP_GUARD = 100000


class DarkTowerInterpreter:
    def __init__(self):
        self.variables: Dict[str, Any] = {}
        self.registers = {f"R{i}": 0 for i in range(8)}
        self.memory = [0] * 4096
        self.output: List[Any] = []
        self.labels: Dict[str, int] = {}

    def _safe_name(self, name: str) -> Any:
        if name in self.variables:
            return self.variables[name]
        if name in self.registers:
            return self.registers[name]
        if name == "TRUE":
            return 1
        if name == "FALSE":
            return 0
        if name == "PI":
            return math.pi
        raise NameError(f"Unknown symbol: {name}")

    def _eval_expr(self, expression: str) -> Any:
        try:
            node = ast.parse(expression, mode="eval")
        except SyntaxError as exc:
            raise ValueError(f"Invalid expression: {expression}") from exc
        return self._eval_node(node.body)

    def _eval_node(self, node: ast.AST) -> Any:
        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.Name):
            return self._safe_name(node.id)

        if isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            op = ALLOWED_BINOPS.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
            return op(left, right)

        if isinstance(node, ast.UnaryOp):
            operand = self._eval_node(node.operand)
            op = ALLOWED_UNARYOPS.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
            return op(operand)

        if isinstance(node, ast.BoolOp):
            values = [self._eval_node(v) for v in node.values]
            op = ALLOWED_BOOLOPS.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported boolean operator: {type(node.op).__name__}")
            result = values[0]
            for value in values[1:]:
                result = op(result, value)
            return result

        if isinstance(node, ast.Compare):
            left = self._eval_node(node.left)
            for comparator, next_node in zip(node.ops, node.comparators):
                right = self._eval_node(next_node)
                op = ALLOWED_CMPOPS.get(type(comparator))
                if op is None:
                    raise ValueError(f"Unsupported comparison: {type(comparator).__name__}")
                if not op(left, right):
                    return 0
                left = right
            return 1

        if isinstance(node, ast.IfExp):
            condition = self._eval_node(node.test)
            if condition:
                return self._eval_node(node.body)
            return self._eval_node(node.orelse)

        raise ValueError(f"Unsupported expression node: {type(node).__name__}")

    def _strip_comment(self, line: str) -> str:
        if "#" in line:
            line = line.split("#", 1)[0]
        if ";" in line:
            line = line.split(";", 1)[0]
        return line.strip()

    def _build_labels(self, lines: List[str]) -> None:
        for idx, line in enumerate(lines):
            if not line:
                continue
            label_match = re.match(r"^LABEL\s+([A-Za-z_][A-Za-z0-9_]*)\s*$", line, re.IGNORECASE)
            if label_match:
                self.labels[label_match.group(1)] = idx

    def _find_matching_end(self, lines: List[str], start_index: int, start_word: str, end_word: str) -> int:
        depth = 0
        for idx in range(start_index, len(lines)):
            line = lines[idx]
            if re.match(rf"^\s*{start_word}\b", line, re.IGNORECASE):
                depth += 1
            if re.match(rf"^\s*{end_word}\b", line, re.IGNORECASE):
                depth -= 1
                if depth == 0:
                    return idx
        raise ValueError(f"Missing matching {end_word} for {start_word}")

    def execute_source(self, source: str):
        lines = [self._strip_comment(line) for line in source.splitlines()]
        lines = [line for line in lines if line]
        self._build_labels(lines)
        index = 0

        while index < len(lines):
            line = lines[index]

            if re.match(r"^LABEL\s+", line, re.IGNORECASE):
                index += 1
                continue

            if re.match(r"^SET\s+", line, re.IGNORECASE):
                match = re.match(r"^SET\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+)$", line, re.IGNORECASE)
                if not match:
                    raise ValueError(f"Invalid assignment: {line}")
                name, expr = match.groups()
                self.variables[name] = self._eval_expr(expr)
                index += 1
                continue

            if re.match(r"^PRINT\s+", line, re.IGNORECASE):
                expr = line[6:].strip()
                value = self._eval_expr(expr)
                self.output.append(value)
                print(value)
                index += 1
                continue

            if re.match(r"^IF\b", line, re.IGNORECASE):
                match = re.match(r"^IF\s+(.+)\s+THEN\s*$", line, re.IGNORECASE)
                if not match:
                    raise ValueError(f"Invalid IF statement: {line}")
                condition = match.group(1)
                end_index = self._find_matching_end(lines, index + 1, "IF", "ENDIF")
                if self._eval_expr(condition):
                    block_index = index + 1
                    while block_index < end_index:
                        block_line = lines[block_index]
                        if re.match(r"^ENDIF\b", block_line, re.IGNORECASE):
                            break
                        block_index = self._execute_block(lines, block_index)
                    index = end_index + 1
                else:
                    index = end_index + 1
                continue

            if re.match(r"^WHILE\b", line, re.IGNORECASE):
                match = re.match(r"^WHILE\s+(.+)\s+DO\s*$", line, re.IGNORECASE)
                if not match:
                    raise ValueError(f"Invalid WHILE statement: {line}")
                condition = match.group(1)
                end_index = self._find_matching_end(lines, index + 1, "WHILE", "ENDWHILE")
                loops = 0
                while self._eval_expr(condition):
                    loops += 1
                    if loops > MAX_LOOP_GUARD:
                        raise RuntimeError("Maximum loop guard exceeded; loop may be infinite")
                    block_index = index + 1
                    while block_index < end_index:
                        block_line = lines[block_index]
                        if re.match(r"^ENDWHILE\b", block_line, re.IGNORECASE):
                            break
                        block_index = self._execute_block(lines, block_index)
                    index = index + 1
                    if index >= len(lines):
                        break
                index = end_index + 1
                continue

            if re.match(r"^GOTO\s+", line, re.IGNORECASE):
                target = re.match(r"^GOTO\s+([A-Za-z_][A-Za-z0-9_]*)\s*$", line, re.IGNORECASE)
                if not target:
                    raise ValueError(f"Invalid GOTO statement: {line}")
                destination = target.group(1)
                if destination not in self.labels:
                    raise ValueError(f"Unknown label: {destination}")
                index = self.labels[destination]
                continue

            if re.match(r"^HALT\b", line, re.IGNORECASE):
                break

            raise ValueError(f"Unsupported statement: {line}")

        return self.output

    def _execute_block(self, lines: List[str], start_index: int) -> int:
        line = lines[start_index]
        if re.match(r"^SET\s+", line, re.IGNORECASE):
            match = re.match(r"^SET\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+)$", line, re.IGNORECASE)
            if not match:
                raise ValueError(f"Invalid assignment: {line}")
            name, expr = match.groups()
            self.variables[name] = self._eval_expr(expr)
            return start_index + 1

        if re.match(r"^PRINT\s+", line, re.IGNORECASE):
            value = self._eval_expr(line[6:].strip())
            self.output.append(value)
            print(value)
            return start_index + 1

        if re.match(r"^IF\b", line, re.IGNORECASE):
            match = re.match(r"^IF\s+(.+)\s+THEN\s*$", line, re.IGNORECASE)
            if not match:
                raise ValueError(f"Invalid IF statement: {line}")
            condition = match.group(1)
            end_index = self._find_matching_end(lines, start_index + 1, "IF", "ENDIF")
            if self._eval_expr(condition):
                block_index = start_index + 1
                while block_index < end_index:
                    block_line = lines[block_index]
                    if re.match(r"^ENDIF\b", block_line, re.IGNORECASE):
                        break
                    block_index = self._execute_block(lines, block_index)
                return end_index + 1
            return end_index + 1

        if re.match(r"^WHILE\b", line, re.IGNORECASE):
            match = re.match(r"^WHILE\s+(.+)\s+DO\s*$", line, re.IGNORECASE)
            if not match:
                raise ValueError(f"Invalid WHILE statement: {line}")
            condition = match.group(1)
            end_index = self._find_matching_end(lines, start_index + 1, "WHILE", "ENDWHILE")
            while self._eval_expr(condition):
                block_index = start_index + 1
                while block_index < end_index:
                    block_line = lines[block_index]
                    if re.match(r"^ENDWHILE\b", block_line, re.IGNORECASE):
                        break
                    block_index = self._execute_block(lines, block_index)
            return end_index + 1

        if re.match(r"^HALT\b", line, re.IGNORECASE):
            return start_index + 1

        if re.match(r"^LABEL\s+", line, re.IGNORECASE):
            return start_index + 1

        if re.match(r"^GOTO\s+", line, re.IGNORECASE):
            return start_index + 1

        raise ValueError(f"Unsupported block statement: {line}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 dark_tower_interpreter.py <source-file>")
        return 1

    source_path = Path(sys.argv[1])
    if not source_path.exists():
        print(f"File not found: {source_path}")
        return 1

    try:
        interpreter = DarkTowerInterpreter()
        source = source_path.read_text(encoding="utf-8")
        interpreter.execute_source(source)
        print("Dark Tower interpreter finished.")
    except Exception as exc:
        print(f"Dark Tower interpreter error: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
