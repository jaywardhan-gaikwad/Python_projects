# Email Validator

A simple Python script that validates an email address by checking for lowercase letters, spaces, the '@' symbol, and domain correctness.  
It provides clear, colorful feedback in the terminal using the `rich` library.

## Features
- Validates email format step by step  
- Detects missing '@' or domain parts  
- Warns if the email includes uppercase letters or spaces  
- Displays readable, color-coded messages  

## How to Run
Install the required library:
```bash
pip install rich
