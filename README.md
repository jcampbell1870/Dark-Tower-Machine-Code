# Dark Tower Operating System

The Dark Tower Operating System is a conceptual IBM-inspired operating environment designed to power Dark Tower-based computers, training systems, and educational machine-code platforms.

This project is structured as a small but increasingly realistic operating system with:

- boot sequence and bootloader support
- a kernel-style runtime layer
- command shell interaction
- file system support
- process management
- scheduler support
- memory and register monitoring
- system call handling
- console session management
- high-level language interpretation and execution

## Included components

- `src/dark_tower_vm.py` — Dark Tower virtual machine
- `src/dark_tower_assembler.py` — assembler
- `src/dark_tower_translator.py` — source translator
- `src/dark_tower_os.py` — OS execution runtime
- `src/dark_tower_kernel.py` — kernel command and control layer
- `src/dark_tower_shell.py` — interactive system shell
- `src/dark_tower_interpreter.py` — high-level source interpreter
- `src/dark_tower_filesystem.py` — lightweight file system
- `src/dark_tower_process_manager.py` — process manager
- `src/dark_tower_scheduler.py` — scheduling queue and dispatcher
- `src/dark_tower_bootloader.py` — system bootloader
- `src/dark_tower_monitor.py` — operational monitoring dashboard
- `src/dark_tower_system_calls.py` — Dark Tower system call interface
- `src/dark_tower_console.py` — textual console and shell session manager

## Boot and system startup

Run the shell:

```bash
python3 src/dark_tower_shell.py
```

Use commands such as:

```text
boot
bootloader
run examples/hello.dt
interpret examples/hello.dt
status
memory 32
ls
processes
scheduler
monitor
help
quit
```

## Bootloader

The Dark Tower bootloader provides a system startup routine similar to a real computer boot process. It initializes the machine state, loads processes, and prepares the runtime for execution.

## Scheduler and process model

The scheduler demonstrates how a basic operating system could manage a ready queue and process lifecycle. This keeps the project educational while making it feel more like a real computer OS instead of only a virtual machine.

## File system and shell operations

The system includes a simple in-memory file system for maintaining text-based resources. The shell allows users to browse files, create or remove files, and inspect system state.

## System calls and console services

The Dark Tower OS includes a simple system call model for operations such as:

- `read` from a file or stream
- `write` to output or a file
- `status` for hardware and process information
- `memdump` for memory inspection
- `run` to start a process

This function set gives the system a practical OS-style interface without turning the project into production code.

## Machine language and interpreter

The Dark Tower environment supports:

- assembly-style instructions
- translator-based source processing
- a full interpreter for a high-level Dark Tower language
- execution loops and branching logic

## Learning path

1. Start the shell.
2. Run `bootloader` and `boot`.
3. Open `examples/hello.dt` and run it.
4. Use `interpret` with a source script.
5. Inspect the scheduler and process queue.
6. Review the monitor and memory output.
7. Exercise the system call and console interfaces.

## License

This project is distributed under the MIT License.
