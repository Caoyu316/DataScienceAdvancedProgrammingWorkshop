# Session 6 exercises — files in, files out
#
# PREDICT tasks are in Wooclap. For the others, write your code under
# "your code here" and press ▷. The setup below WRITES the data files
# into the folder this file is in (HERE), every time you run it, so you
# always start from the same data. Open them in the Explorer to see
# them.

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
# Read and debug
# ════════════════════════════════════════════════════════════════════

# ── Task 1 · PREDICT: the invisible \n ──────────────────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 2 · PREDICT: "w" erases, "a" appends ───────────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 3 · DEBUG: a total with no error, and wrong ────────────────
# A colleague adds up the prices of the four positions in ledger.csv. It
# should print 1214.8. It prints something else, and there is no error
# at all. Which line is the bug? Fix it by changing two characters.
# First answer in Wooclap (which line?), then fix it here.

total = 0.0
with open(ledger_path, encoding="utf-8") as f:
    lines = f.readlines()
for line in lines[1:-1]:
    ticker, name, shares, price = line.strip().split(",")
    total += float(price)
print("Task 3:", round(total, 2))


# ── Task 4 · PREDICT: try, row by row ───────────────────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 5 · PREDICT: one gap, a column of floats ───────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.



# ════════════════════════════════════════════════════════════════════
# Write it yourself
# ════════════════════════════════════════════════════════════════════

# ── Task 6 · WRITE: load the ledger by hand ─────────────────────────
# Read ledger.csv with open(): skip the header, split each line, convert
# shares with int() and price with float(). Keep the good rows as
# (ticker, shares, price) tuples in a list; skip a bad row with try /
# except ValueError, printing which ticker you skipped. Then print the
# number of good rows and the total value, rounded to 2.
# You should see:
#   skipped MSFT
#   Task 6: 3 3338.2

# your code here


# ── Task 7 · WRITE: write a report, read it back ────────────────────
# Write report.txt in HERE: one line per good position, "AAPL 1905.00"
# (ticker, a space, the value with 2 decimals), then a last line "total
# 3338.20". Use open(..., "w") and f.write(...); do not forget the "\n".
# Then read the file back and print it.
# You should see:
#   AAPL 1905.00
#   NESN 409.20
#   VOO 1024.00
#   total 3338.20

positions = [("AAPL", 10, 190.5), ("NESN", 4, 102.3), ("VOO", 2, 512.0)]
# your code here


# ── Task 8 · WRITE: the Swiss export ────────────────────────────────
# ledger_eu.csv is the same ledger as Excel exports it in Switzerland: ;
# between fields and , as the decimal mark. First read it with plain
# pd.read_csv and print the columns you get. Then give read_csv the two
# options that fix it, and print the total value.
# You should see:
#   Task 8: ['ticker;shares;price']
#   Task 8: 3338.2

# your code here


# ── Task 9 · WRITE: raise with a clear message ──────────────────────
# Write a function to_shares(text) that returns int(text), but raises
# ValueError("missing shares") when text is the empty string. Then call
# it on "10" and on "" inside a try, and print the result or the error
# message.
# You should see:
#   Task 9: 10
#   Task 9: error: missing shares

# your code here


# ── Task 10 · WRITE: today's prices from a second file ──────────────
# prices_today.csv has the new price of each ticker, in a different
# order. Read it into a dict ticker → price (with open() or with
# pandas), then compute the value of the three good positions at TODAY's
# prices. Print the total, rounded to 2.
# You should see:
#   Task 10: 3322.8

positions = [("AAPL", 10, 190.5), ("NESN", 4, 102.3), ("VOO", 2, 512.0)]
# your code here



# ════════════════════════════════════════════════════════════════════
# ★ Harder: classic puzzles
# ════════════════════════════════════════════════════════════════════

# ── ★ Task 11 · Lines, characters, bytes (the Unix wc classic) ──────
# Read ledger.csv as one string. Print three numbers: how many lines,
# how many characters, and how many BYTES the file takes on disk (len of
# the text encoded in UTF-8, or the file size from pathlib). Characters
# and bytes differ by exactly one. Which letter is responsible?
# You should see:
#   Task 11: 5 112 113 113

# your code here


# ── ★ Task 12 · An error log with line numbers ──────────────────────
# Go through ledger.csv and write errors.txt with one line per bad row:
# its LINE NUMBER in the file (the header is line 1), the ticker and the
# error message. Use enumerate(f, start=1). Print the file afterwards.
# You should see:
#   line 5: MSFT: invalid literal for int() with base 10: ''

# your code here


# ── ★ Task 13 · The last n lines (the Unix tail classic) ────────────
# Write tail(path, n) that returns the last n lines of a file as a list
# of strings without their "\n". It must work for n larger than the
# file, and for n = 0 (watch out: lines[-0:] is the WHOLE list). Print
# tail(ledger_path, 2), tail(ledger_path, 0) and len(tail(ledger_path,
# 99)).
# You should see:
#   Task 13: ['VOO,Vanguard,2,512.00', 'MSFT,Microsoft,,410.00']
#   Task 13: [] 5

# your code here
