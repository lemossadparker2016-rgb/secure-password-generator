# Secure Password Generator 🔐

A lightweight, easy-to-use Python Command Line Interface (CLI) tool to generate cryptographically secure passwords.

## Features
- Uses Python's `secrets` module for maximum security (unlike the standard `random` module).
- Customizable password length.
- Option to include or exclude special symbols.
- Zero dependencies (runs purely on standard Python).

## How to use

1. Make sure you have Python installed on your system.
2. Clone the repository or download the `main.py` file.
3. Run the script in your terminal:

```bash
python main.py

--- Secure Password Generator ---
Enter password length (default is 12): 16
Include special symbols? (y/n, default is y): y

Generating...
Your new secure password is: 7#kL9!mQp2$xR4vB
