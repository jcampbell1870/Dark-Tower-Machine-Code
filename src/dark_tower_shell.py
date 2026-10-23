#!/usr/bin/env python3
"""Dark Tower shell.

This module provides an interactive command shell that gives the user a simple
operating-system style interface for booting, running, interpreting, inspecting,
and managing Dark Tower programs.
"""

from __future__ import annotations

from dark_tower_kernel import DarkTowerKernel


class DarkTowerShell:
    def __init__(self):
        self.kernel = DarkTowerKernel()

    def run(self):
        print(self.kernel.boot_banner)
        print("Type 'help' for commands, 'quit' to exit.")
        while True:
            try:
                command = input("DarkTower> ")
            except EOFError:
                print("\nExiting Dark Tower shell.")
                break
            if not command.strip():
                continue
            result = self.kernel.dispatch(command)
            if result == "QUIT":
                print("Goodbye.")
                break
            if result is not None:
                if isinstance(result, dict):
                    for key, value in result.items():
                        print(f"{key}: {value}")
                else:
                    print(result)


def main():
    shell = DarkTowerShell()
    shell.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
