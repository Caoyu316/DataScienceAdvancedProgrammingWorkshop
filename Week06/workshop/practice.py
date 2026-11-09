# Session 6 extra practice — classics. Optional and ungraded; nothing is
# handed in. Solutions follow a week later.

from pathlib import Path
import pandas as pd

HERE = Path(__file__).parent          # the folder this file is in
(HERE / "ledger.csv").write_text(
    "ticker,name,shares,price\n"
    "AAPL,Apple,10,190.50\n"
    "NESN,Nestlé,4,102.30\n"
    "VOO,Vanguard,2,512.00\n"
    "MSFT,Microsoft,,410.00\n", encoding="utf-8")
(HERE / "ledger_eu.csv").write_text(  # the same ledger, as a Swiss Excel exports it
    "ticker;shares;price\n"
    "AAPL;10;190,50\n"
    "NESN;4;102,30\n"
    "VOO;2;512,00\n", encoding="utf-8")
(HERE / "prices_today.csv").write_text(
    "ticker,price\n"
    "VOO,515.20\n"
    "AAPL,188.00\n"
    "NESN,103.10\n", encoding="utf-8")
ledger_path = HERE / "ledger.csv"


# ════════════════════════════════════════════════════════════════════
# Extra practice: classics (optional, ungraded)
# ════════════════════════════════════════════════════════════════════

# ── Practice 1 · Reverse a file (the Unix tac classic) ──────────────
# Write reversed.csv: the header first, then the data rows of ledger.csv
# in reverse order (MSFT first). Print the file.
# You should see:
#   ticker,name,shares,price
#   MSFT,Microsoft,,410.00
#   AAPL,Apple,10,190.50

# your code here


# ── Practice 2 · Fill the gap instead of dropping it ────────────────
# With pandas: read ledger.csv, replace MSFT's missing shares by 0
# (fillna), convert shares back to int, add a value column, and write
# report.csv without the index. Read report.csv back and print its shape
# and the value column as a list.
# You should see:
#   (4, 5) [1905.0, 409.2, 1024.0, 0.0]

# your code here


# ── Practice 3 · Count by first letter, into a file ─────────────────
# For the tickers of ledger.csv, count how many start with each letter,
# in a dict. Write the counts to counts.txt, one "letter count" per
# line, in alphabetical order. Print the file.
# You should see:
#   A 1
#   M 1
#   N 1
#   V 1

# your code here
