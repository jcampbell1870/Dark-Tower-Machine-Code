#!/usr/bin/env python3
"""Dark Tower kernel runtime.

This kernel exposes a small operating-system style interface to the Dark Tower
machine environment. It provides boot, status, memory, execution, and
interpretation functions that mimic a simple system monitor.
"""

from __future__ import annotations

from pathlib import Path

from dark_tower_interpreter import DarkTowerInterpreter
from dark_tower_os import DarkTowerOS


class DarkTowerKernel:
    def __init__(self):
        self.os = DarkTowerOS()
        self.boot_banner = "\n=== Dark Tower Operating System v1.0 ===\n"

    def boot(self, program_path: str | None = None):
        print(self.boot_banner)
        print("Initializing memory and register file...")
        self.os.registers = {f"R{i}": 0 for i in range(8)}
        self.os.memory = [0] * 4096
        if program_path:
            return self.run_program(program_path)
        print("Boot complete. Ready for system commands.")
        return True

    def help_text(self):
        return """
Dark Tower system commands:
  boot [program]     Start the OS and optionally launch a program
  run <program>      Load and execute a Dark Tower program
  interpret <file>   Interpret a Dark Tower programming-language source file
  status            Display current register state
  memory            Display the first 32 memory cells
  help              Show this text
  quit              Exit the Dark Tower shell
"""

    def status(self):
        return self.os.registers

    def memory_report(self):
        return self.os.memory[:32]

    def run_program(self, program_path: str):
        try:
            print(f"Launching program: {program_path}")
            result = self.os.execute(program_path)
            print("Program completed successfully.")
            return result
        except Exception as exc:
            raise RuntimeError(f"Dark Tower program execution failed: {exc}") from exc

    def interpret(self, program_path: str):
        try:
            path = Path(program_path)
            if not path.exists():
                raise FileNotFoundError(f"Program not found: {path}")
            interpreter = DarkTowerInterpreter()
            source = path.read_text(encoding="utf-8")
            output = interpreter.execute_source(source)
            print("Interpretation complete.")
            return output
        except Exception as exc:
            raise RuntimeError(f"Dark Tower interpreter failed: {exc}") from exc

    def dispatch(self, command: str):
        tokens = command.strip().split()
        if not tokens:
            return None
        verb = tokens[0].lower()
        if verb == "quit":
            return "QUIT"
        if verb == "boot":
            program = tokens[1] if len(tokens) > 1 else None
            return self.boot(program)
        if verb == "run":
            if len(tokens) < 2:
                return "Usage: run <program-file>"
            return self.run_program(tokens[1])
        if verb == "interpret":
            if len(tokens) < 2:
                return "Usage: interpret <source-file>"
            return self.interpret(tokens[1])
        if verb == "status":
            return self.status()
        if verb == "memory":
            return self.memory_report()
        if verb == "help":
            return self.help_text()
        return f"Unknown command: {verb}"


if __name__ == "__main__":
    kernel = DarkTowerKernel()
    print(kernel.boot_banner)
    print("Kernel operational.")
