# Dark Tower Interpreter Guide

This guide explains how to use the Dark Tower interpreter, the executable language runtime, and the main language features.

## Overview

The Dark Tower interpreter is a computer-programming language runtime designed for the Dark Tower operating system. It is not a full-scale production language but it is a capable educational interpreter for machine-level and system-style programming.

It supports:

- variable assignment
- arithmetic expressions
- printing values
- conditionals
- loops
- labels and jumps
- `HALT` to terminate execution

## Running the interpreter

From the repository root:

```bash
python3 src/dark_tower_interpreter.py my_program.dt
```

This executes the instructions defined in the file.

## Example program

```text
SET total = 7
SET count = 5
SET result = total + count
PRINT result
HALT
```

This creates variables, adds them, prints the result, and exits.

## Language features

### Assignment

```text
SET x = 10
SET y = x + 5
```

### Output

```text
PRINT x
```

### Conditionals

```text
IF x > 0 THEN
  PRINT x
ENDIF
```

### Looping

```text
SET counter = 0
WHILE counter < 5 DO
  PRINT counter
  SET counter = counter + 1
ENDWHILE
```

### Labels and jumps

```text
LABEL start
SET x = x + 1
IF x < 10 THEN
  GOTO start
ENDIF
HALT
```

## Best practices

- keep variable names readable
- verify condition logic
- use labels for repeated blocks
- insert prints when debugging logic
- keep routines short and focused

## Relationship to the OS

The interpreter is designed to work alongside the Dark Tower operating environment. Programs may be run directly, through the shell, or as samples used to teach machine execution and operating-system logic.
