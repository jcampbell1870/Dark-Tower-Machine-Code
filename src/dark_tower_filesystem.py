#!/usr/bin/env python3
"""Dark Tower filesystem abstraction.

This module provides a lightweight file system model for the Dark Tower OS.
It is deliberately small and educational, designed to support basic file
management, command-line browsing, and system operation demonstration.
"""

from __future__ import annotations

from typing import Dict, List


class DarkTowerFileSystem:
    def __init__(self):
        self.files: Dict[str, str] = {
            "README.txt": "Dark Tower Operating System\n",
            "boot.log": "System initialized successfully.\n",
            "programs.txt": "hello.dt\nfactorial.dt\n",
        }

    def list_files(self) -> List[str]:
        return sorted(self.files.keys())

    def read(self, filename: str) -> str:
        if filename not in self.files:
            raise FileNotFoundError(f"File not found: {filename}")
        return self.files[filename]

    def write(self, filename: str, content: str) -> str:
        self.files[filename] = content
        return f"Saved: {filename}"

    def remove(self, filename: str) -> str:
        if filename not in self.files:
            raise FileNotFoundError(f"File not found: {filename}")
        del self.files[filename]
        return f"Deleted: {filename}"

    def exists(self, filename: str) -> bool:
        return filename in self.files


if __name__ == "__main__":
    fs = DarkTowerFileSystem()
    print(fs.list_files())
    print(fs.read("README.txt"))
