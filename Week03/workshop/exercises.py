# Session 3 exercises — lists, loops, decisions, dicts
#
# Same rules as yesterday: PREDICT means write your prediction in the
# comment before you press ▷. Each task prints its own label. Write your
# own code under "your code here". ★ tasks are classic programming
# puzzles, dressed as ledger problems; they go from easier to harder.

tickers = ["AAPL", "NESN", "VOO"]
shares = [10, 4, 2]
price = {"AAPL": 190.5, "NESN": 102.3, "VOO": 512.0}
closes = [190.5, 187.2, 193.8, 185.1, 191.4, 198.6, 194.0]   # AAPL, day 0 to day 6


# ════════════════════════════════════════════════════════════════════
# Read and debug
# ════════════════════════════════════════════════════════════════════

# ── Task 1 · PREDICT: slices ────────────────────────────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 2 · PREDICT: a copy, or a second name? ─────────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 3 · DEBUG: the zip that lies ───────────────────────────────
# The total of the ledger is 3338.2. Someone wanted the positions "in
# order" and put sorted(shares) inside the zip. It runs, and prints a
# total that looks like money.
#
# First fill in an iteration table ON PAPER (ticker, shares, value,
# running total), then explain what went wrong and fix it.
# First answer in Wooclap (which line?), then fix it here.

total = 0.0
for t, n in zip(tickers, sorted(shares)):
    total += n * price[t]
print("Task 3:", total)


# ── Task 4 · DEBUG: the boundary ────────────────────────────────────
# The broker's rule: "positions of 1000 CHF or more pay a 0.1 % fee". A
# position of 8 shares at 125.00 is exactly 1000.00 CHF. The code says
# it pays nothing. Who is right? Fix the code.
# First answer in Wooclap (which line?), then fix it here.

value = 8 * 125.0
if value > 1000:
    fee = value * 0.001
else:
    fee = 0.0
print("Task 4:", value, fee)


# ── Task 5 · PREDICT: a price that is not there ─────────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.



# ════════════════════════════════════════════════════════════════════
# Write it yourself
# ════════════════════════════════════════════════════════════════════

# ── Task 6 · WRITE: from text to a total ────────────────────────────
# A ledger file arrives as lines of text. Loop over the lines, cut each
# one at the commas with .split(","), convert the pieces, and add up the
# value.
# You should see:
#   Task 6: 3338.2

lines = ["AAPL,10,190.50", "NESN,4,102.30", "VOO,2,512.00"]

# your code here


# ── Task 7 · WRITE: the largest position, without max() ─────────────
# Find which position is worth the most, and print its ticker and value.
# Do not use max(): keep "the best so far" in two names and update them.
# Loop with zip(tickers, shares).
# You should see:
#   Task 7: AAPL 1905.00

# your code here


# ── Task 8 · WRITE: yesterday's lie, fixed ──────────────────────────
# Yesterday, cash_from_file or 1000.0 turned a real balance of 0.0 into
# 1000.0. Now you have if. Write it so that ONLY a missing value (None)
# becomes 1000.0, and 0.0 stays 0.0. Try it on 250.0, 0.0 and None.
# You should see:
#   Task 8: 250.0 -> 250.0
#   Task 8: 0.0 -> 0.0
#   Task 8: None -> 1000.0

# your code here


# ── Task 9 · WRITE: ask before you look up ──────────────────────────
# Loop over the tickers AAPL, MSFT, VOO. For each one, print its price,
# or "no price" if the dict does not have it. Write it once with in, and
# once with .get().
# You should see:
#   Task 9: AAPL 190.5
#   Task 9: MSFT no price
#   Task 9: VOO 512.0

wanted = ["AAPL", "MSFT", "VOO"]

# your code here


# ── Task 10 · WRITE: how many years until 1500? ─────────────────────
# 1000.00 CHF grows by 3 % a year. After how many whole years is it
# worth at least 1500.00? Nobody knows the number of passes in advance,
# so use while. Print the years and the value then.
# You should see:
#   Task 10: 14 1512.59

value = 1000.0

# your code here



# ════════════════════════════════════════════════════════════════════
# ★ Harder: classic puzzles
# ════════════════════════════════════════════════════════════════════

# ── ★ Task 11 · Running total, and the worst moment ─────────────────
# Daily profit and loss of a portfolio, in CHF. Build the list of
# running totals after each day, and find the lowest the running total
# ever got.
# You should see:
#   Task 11: [120.0, -220.5, -140.25, -200.25, 209.75, 114.0]
#   Task 11: worst -220.5

pnl = [120.0, -340.5, 80.25, -60.0, 410.0, -95.75]

# your code here


# ── ★ Task 12 · The trade that appears twice ────────────────────────
# A list of trades in the order they arrived. Count how many times each
# ticker appears (a dict, with .get()), and print the FIRST ticker that
# shows up a second time.
# You should see:
#   Task 12: {'AAPL': 2, 'NESN': 2, 'VOO': 1} NESN

trades = ["AAPL", "NESN", "VOO", "NESN", "AAPL"]

# your code here


# ── ★ Task 13 · Two sum: spend the budget exactly ───────────────────
# One share each of two DIFFERENT stocks must cost exactly 614.30 CHF.
# Which two? Prices are in cents, so == is safe.
#
# Step 1: two loops, one inside the other, so that every pair is tried
# once. Step 2 (★★): one loop only, with enumerate(). Keep a dict of the
# prices already seen; for each price, ask "have I seen the price that
# completes it?".
# You should see:
#   Task 13: NESN VOO

all_tickers = ["AAPL", "NESN", "VOO", "MSFT", "NOVN"]
all_prices_c = [19050, 10230, 51200, 41000, 8870]
budget_c = 61430

# your code here


# ── ★ Task 14 · Best day to buy, best day to sell ───────────────────
# The daily closes of AAPL for a week (day 0 to day 6). You may buy once
# and sell once, later. What is the largest profit, and on which days?
# One loop with enumerate() is enough: remember the lowest price so far,
# and ask every day "what if I sold today?".
# You should see:
#   Task 14: buy day 3, sell day 5, profit 13.50

# your code here


# ── ★ Task 15 · numpy: slicing in two directions ────────────────────
# Pavel's slices.py showed a numpy table: one row per position, column 0
# = shares, column 1 = price. With numpy, [rows, columns] slices both
# directions at once. On paper, predict all five lines, then run and
# check. What does the last line compute, and why does it not need a
# loop?

import numpy as np
table = np.array([[10, 190.5], [4, 102.3], [2, 512.0]])   # rows: AAPL, NESN, VOO

print("Task 15:", table[1:, 0])
print("Task 15:", table[:2, 1])
print("Task 15:", table[-1])
print("Task 15:", table[::2, 1])
print("Task 15:", table[:, 0] * table[:, 1])
