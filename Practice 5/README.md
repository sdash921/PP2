# Practice 5: Python RegEx Receipt Parser

## Overview
This project demonstrates the use of Python's `re` module to parse unstructured text from a retail receipt.

## Regex Patterns Used
- **Date**: `\d{2}/\d{2}/\d{4}` — Matches the DD/MM/YYYY format.
- **Prices**: `\$(\d+\.\d{2})` — Captures numerical values following a dollar sign.
- **Product Names**: `\d+x\s+(.*?)\s+\.*\$` — Uses a non-greedy match `(.*?)` to capture text between the quantity and the price-padding dots.
- **Payment Method**: `PAYMENT METHOD:\s*(.*)` — Captures all characters following the payment header.

## How to Run
1. Ensure `raw.txt` and `receipt_parser.py` are in the same directory.
2. Run the script:
   ```bash
   python receipt_parser.py