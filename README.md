# Unix Permissions Calculator

A simple interactive Python tool that generates Unix/Linux file permission strings in both **symbolic** (e.g., `-rwxr-xr-x`) and **numeric octal** (e.g., `755`) formats based on your answers.

## Features

- Asks for file type: directory (`d`), regular file (`-`), or symbolic link (`l`).
- Asks for read, write, execute permissions separately for **owner**, **group**, and **others** (yes/no).
- Validates all inputs – only accepts `d`, `-`, `l` for file type and `y`/`n` for permissions.
- Displays the final Unix permission string (e.g., `-rw-r--r--`) and the octal numeric code (e.g., `644`).

## Requirements

- Python 3.x (no external libraries)

## Usage

1. Save the script as `calculate_unix_permissions.py`.
2. Open a terminal/command prompt in the script's folder.
3. Run the script:
   ```command line
   python calculate_unix_permissions.py
   ```

## How The Calculation Works
- Symbolic: Each permission is shown as r (read), w (write), x (execute), or - (no permission). The order is always: file type, owner, group, others.
- Numeric (octal): Each group (owner, group, others) gets a digit from 0 to 7, where:
    - read = 4
    - write = 2
    - execute = 1
    - Sum of enabled permissions.

## Notes
- This script only calculates permissions – it does not modify any real files.
-For symbolic links, the permissions shown are those you entered (though real Unix symlinks often have `lrwxrwxrwx` and the actual permissions are ignored). Use the script as a learning tool for permission strings.

## Author: DanyByte
