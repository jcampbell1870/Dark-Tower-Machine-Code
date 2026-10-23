# Dark Tower System Calls Guide

This guide describes the Dark Tower system call interface and how it supports operating-system-style behavior in the project.

## Overview

The Dark Tower OS includes a lightweight system-call model. Although simple and educational, it helps demonstrate how a user program or shell command requests a service from the kernel or runtime environment.

The system call layer supports:

- reading files or resources
- writing output to a file or stream
- checking machine status
- reading memory for diagnostics
- launching a program
- retrieving help text

## Example system calls

```text
read README.txt
write output.txt Hello Dark Tower
status
memdump 16
run examples/hello.dt
help
```

## Core responsibilities

### `read`
Reads an existing in-memory file or resource.

### `write`
Creates or updates a file or output target.

### `status`
Returns register and system state information.

### `memdump`
Returns a slice of memory to be analyzed or displayed.

### `run`
Launches a system program or script.

### `help`
Shows available system calls and usage.

## Relationship to the OS

The system call layer sits between the user shell and the lower-level runtime. It provides a simple interface that mimics how an operating system commonly routes requests from user programs into privileged services.

## Best practices

- keep system calls small and explicit
- validate file existence before read or write operations
- return status responses in readable structures
- separate user-facing output from kernel/service logic

## Summary

The Dark Tower system call layer is intentionally simple but effective for teaching operating-system concepts, resource management, and user-to-kernel communication in a compact environment.
