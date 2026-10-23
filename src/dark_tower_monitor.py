#!/usr/bin/env python3
"""Dark Tower system monitor.

The monitor provides a user-friendly snapshot of the OS state, including
registers, system memory, filesystem contents, and active processes.
"""

from __future__ import annotations

from typing import Any


class DarkTowerMonitor:
    def __init__(self, kernel):
        self.kernel = kernel

    def render(self) -> str:
        registers = self.kernel.os.registers if hasattr(self.kernel.os, "registers") else {}
        memory = self.kernel.os.memory[:16] if hasattr(self.kernel.os, "memory") else []
        files = self.kernel.filesystem.list_files() if hasattr(self.kernel, "filesystem") else []
        procs = self.kernel.process_manager.list_processes() if hasattr(self.kernel, "process_manager") else []

        lines = [
            "=== Dark Tower OS Monitor ===",
            "Registers:",
        ]
        for key, value in registers.items():
            lines.append(f"  {key}: {value}")

        lines.append("Memory (first 16 cells):")
        for index, value in enumerate(memory):
            lines.append(f"  MEM[{index}]: {value}")

        lines.append("Files:")
        for name in files:
            lines.append(f"  {name}")

        lines.append("Processes:")
        if procs:
            for proc in procs:
                lines.append(
                    f"  PID {proc['pid']} | {proc['name']} | {proc['status']} | {proc['memory_usage']} bytes"
                )
        else:
            lines.append("  No active processes.")

        return "\n".join(lines)
