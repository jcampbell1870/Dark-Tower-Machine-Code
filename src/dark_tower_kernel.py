#!/usr/bin/env python3
"""Dark Tower kernel runtime.

This kernel exposes a small operating-system style interface to the Dark Tower
machine environment. It provides boot, status, memory, execution, file-system,
and process-management services.
"""

from __future__ import annotations

from pathlib import Path

from dark_tower_filesystem import DarkTowerFileSystem
from dark_tower_interpreter import DarkTowerInterpreter
from dark_tower_os import DarkTowerOS
from dark_tower_process_manager import ProcessManager


class DarkTowerKernel:
    def __init__(self):
        self.os = DarkTowerOS()
        self.filesystem = DarkTowerFileSystem()
        self.process_manager = ProcessManager()
        self.boot_banner = "\n=== Dark Tower Operating System v1.1 ===\n"
        self.history = []

    def boot(self, program_path: str | None = None):
        print(self.boot_banner)
        print("Initializing memory, register file, process queue, and filesystem...")
        self.os.registers = {f"R{i}": 0 for i in range(8)}
        self.os.memory = [0] * 4096
        self.process_manager.processes.clear()
        if program_path:
            return self.run_program(program_path)
        print("Boot complete. Ready for system commands.")
        return True

    def help_text(self):
        return """
Dark Tower system commands:
  boot [program]       Start the OS and optionally launch a program
  run <program>        Load and execute a Dark Tower program
  interpret <file>     Interpret a Dark Tower programming-language source file
  status              Display current register state
  registers           Display register values in a compact form
  memory [count]      Display memory cells; default is 32
  ls                  List files in the Dark Tower filesystem
  cat <file>          Display the contents of a file
  write <file>        Save content to a file
  rm <file>           Remove a file
  processes           List active processes in the system
  monitor             Show a full OS status dashboard
  history             Show command history
  help                Show this text
  quit                Exit the Dark Tower shell
"""

    def status(self):
        return self.os.registers

    def registers(self):
        return self.os.registers

    def memory_report(self, count: int = 32):
        return self.os.memory[:count]

    def run_program(self, program_path: str):
        try:
            print(f"Launching program: {program_path}")
            proc = self.process_manager.start_process(Path(program_path).name, f"run {program_path}")
            result = self.os.execute(program_path)
            proc.status = "COMPLETED"
            print("Program completed successfully.")
            return result
        except Exception as exc:
            raise RuntimeError(f"Dark Tower program execution failed: {exc}") from exc

    def interpret(self, program_path: str):
        try:
            path = Path(program_path)
            if not path.exists():
                raise FileNotFoundError(f"Program not found: {path}")
            proc = self.process_manager.start_process(path.name, f"interpret {program_path}")
            interpreter = DarkTowerInterpreter()
            source = path.read_text(encoding="utf-8")
            output = interpreter.execute_source(source)
            proc.status = "COMPLETED"
            print("Interpretation complete.")
            return output
        except Exception as exc:
            raise RuntimeError(f"Dark Tower interpreter failed: {exc}") from exc

    def ls_files(self):
        return self.filesystem.list_files()

    def cat_file(self, filename: str):
        return self.filesystem.read(filename)

    def write_file(self, filename: str, content: str):
        return self.filesystem.write(filename, content)

    def remove_file(self, filename: str):
        return self.filesystem.remove(filename)

    def list_processes(self):
        return self.process_manager.list_processes()

    def monitor(self):
        from dark_tower_monitor import DarkTowerMonitor
        return DarkTowerMonitor(self).render()

    def dispatch(self, command: str):
        tokens = command.strip().split()
        if not tokens:
            return None
        self.history.append(command)
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
        if verb == "registers":
            return self.registers()
        if verb == "memory":
            count = int(tokens[1]) if len(tokens) > 1 else 32
            return self.memory_report(count)
        if verb == "ls":
            return self.ls_files()
        if verb == "cat":
            if len(tokens) < 2:
                return "Usage: cat <file>"
            return self.cat_file(tokens[1])
        if verb == "write":
            if len(tokens) < 3:
                return "Usage: write <file> <content>"
            filename = tokens[1]
            content = " ".join(tokens[2:])
            return self.write_file(filename, content)
        if verb == "rm":
            if len(tokens) < 2:
                return "Usage: rm <file>"
            return self.remove_file(tokens[1])
        if verb == "processes":
            return self.list_processes()
        if verb == "monitor":
            return self.monitor()
        if verb == "history":
            return self.history
        if verb == "help":
            return self.help_text()
        return f"Unknown command: {verb}"


if __name__ == "__main__":
    kernel = DarkTowerKernel()
    print(kernel.boot_banner)
    print("Kernel operational.")
