#!/usr/bin/env python3
"""Dark Tower process manager.

This module models a simple process and task manager for the Dark Tower OS.
It makes the environment feel more operating-system-like by tracking active
program tasks and their status.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Process:
    pid: int
    name: str
    status: str = "READY"
    command: str = ""
    memory_usage: int = 0


class ProcessManager:
    def __init__(self):
        self._next_pid = 1
        self.processes: Dict[int, Process] = {}

    def start_process(self, name: str, command: str = "") -> Process:
        pid = self._next_pid
        self._next_pid += 1
        proc = Process(pid=pid, name=name, status="RUNNING", command=command, memory_usage=len(command) or 128)
        self.processes[pid] = proc
        return proc

    def list_processes(self) -> List[Dict[str, object]]:
        return [
            {
                "pid": p.pid,
                "name": p.name,
                "status": p.status,
                "command": p.command,
                "memory_usage": p.memory_usage,
            }
            for p in self.processes.values()
        ]

    def terminate(self, pid: int) -> str:
        if pid not in self.processes:
            raise KeyError(f"Unknown process ID: {pid}")
        proc = self.processes.pop(pid)
        proc.status = "TERMINATED"
        return f"Process {pid} ({proc.name}) terminated."


if __name__ == "__main__":
    pm = ProcessManager()
    proc = pm.start_process("hello.dt", "run hello.dt")
    print(proc)
    print(pm.list_processes())
