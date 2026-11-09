# Session 5 exercises — reading data code
#
# PREDICT tasks are in Wooclap. For the others, write your code under
# "your code here" and press ▷. Every task starts from the three
# versions of the same ledger defined below: nested dicts, a numpy grid,
# a pandas table. Rows of the grid are AAPL, NESN, VOO; columns are day
# 0, day 1, day 2.

import numpy as np
import pandas as pd

ledger = {
    "AAPL": {"shares": 10, "prices": [185.0, 188.2, 190.5]},
    "NESN": {"shares": 4, "prices": [104.1, 103.0, 102.3]},
    "VOO": {"shares": 2, "prices": [505.0, 509.9, 512.0]},
}
tickers = np.array(["AAPL", "NESN", "VOO"])
shares = np.array([10, 4, 2])
prices = np.array([[185.0, 188.2, 190.5],
                   [104.1, 103.0, 102.3],
                   [505.0, 509.9, 512.0]])
df = pd.DataFrame({"ticker": ["AAPL", "MSFT", "NESN", "VOO"],
                   "sector": ["tech", "tech", "food", "fund"],
                   "shares": [10, 3, 4, 2],
                   "price": [190.5, 410.0, 102.3, 512.0]})
df["value"] = df["shares"] * df["price"]


# ════════════════════════════════════════════════════════════════════
# Read and debug
# ════════════════════════════════════════════════════════════════════

# ── Task 1 · PREDICT: chains of look-ups ────────────────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 2 · PREDICT: say it in one sentence ────────────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 3 · PREDICT: count the scalars, get the shape ──────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 4 · DEBUG: the scenario that changed the data ──────────────
# A colleague asks "what if NESN's last price were 0?" and tries it on a
# copy of the NESN row. Then they compute the REAL portfolio value,
# which should still be 3338.2. It prints something else. Find the line
# that is the problem, explain it, and fix it with one method call.
# First answer in Wooclap (which line?), then fix it here.

scenario = prices[1]
scenario[-1] = 0
real_values = shares * prices[:, -1]
print("Task 4:", real_values.sum())


# ── Task 5 · PREDICT: labels or positions? ──────────────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.



# ════════════════════════════════════════════════════════════════════
# Write it yourself
# ════════════════════════════════════════════════════════════════════

# ── Task 6 · WRITE: a dict comprehension ────────────────────────────
# In ONE dict comprehension over ledger.items(), build: each ticker →
# its change from the first to the last price, in percent, rounded to 2
# decimals. Print it.
# You should see:
#   Task 6: {'AAPL': 2.97, 'NESN': -1.73, 'VOO': 1.39}

change = {}

# your code here
change = 


# ── Task 7 · WRITE: sort by yesterday's return ──────────────────────
# Sort the tickers of ledger by their LAST daily return (last price /
# the price before it − 1), largest first. Use sorted with key= and a
# lambda.
# You should see:
#   Task 7: ['AAPL', 'VOO', 'NESN']

# your code here


# ── Task 8 · WRITE: the portfolio on every day, no loop ─────────────
# With broadcasting: compute the value of every position on every day (a
# 3 × 3 array), then the portfolio total per day (one number per day),
# then the portfolio's daily return in percent, rounded to 2. No loops.
# Check one number by hand: AAPL on day 0 is 10 × 185 = 1850.
# You should see:
#   Task 8: [3276.4 3313.8 3338.2] [1.14 0.74]

# your code here


# ── Task 9 · WRITE: which positions rose every day? ─────────────────
# Compute the daily returns of every position (a 3 × 2 array, two
# shifted slices). Then, with a mask and axis, find the tickers whose
# return was positive on BOTH days. Print them as a list.
# You should see:
#   Task 9: ['AAPL', 'VOO']

# your code here


# ── Task 10 · WRITE: two pandas questions ───────────────────────────
# (a) The tickers of the TECH positions worth more than 1000 CHF, as a
# list. Two conditions: use &, with parentheses. (b) The total value per
# sector, largest first, as a dict.
# You should see:
#   Task 10a: ['AAPL', 'MSFT']
#   Task 10b: {'tech': 3135.0, 'fund': 1024.0, 'food': 409.2}

# your code here



# ════════════════════════════════════════════════════════════════════
# ★ Harder: classic puzzles
# ════════════════════════════════════════════════════════════════════

# ── ★ Task 11 · Rebase every row to 100 (numpy-100 style) ───────────
# Divide every row by its own day-0 price and multiply by 100, so each
# position starts at 100. One line, with broadcasting: the day-0 column
# must keep its column shape. Round to 2 and print as a list.
# You should see:
#   Task 11: [[100.0, 101.73, 102.97], [100.0, 98.94, 98.27], [100.0, 100.97, 101.39]]

# your code here


# ── ★ Task 12 · Tickers traded more than once (LeetCode pandas: duplicates) ────
# A table of trades. Which tickers appear more than once? Use
# value_counts() and a mask on the result. Then, as a second line, the
# net quantity per ticker with groupby.
# You should see:
#   Task 12: ['AAPL', 'VOO']
#   Task 12: {'AAPL': 4, 'MSFT': 4, 'NESN': 2, 'VOO': 0}

trades = pd.DataFrame({"ticker": ["AAPL", "NESN", "AAPL", "VOO", "MSFT", "AAPL", "VOO"],
                       "qty": [5, 2, -3, 1, 4, 2, -1]})

# your code here


# ── ★ Task 13 · Moving average with cumsum (numpy-100 classic) ──────
# Session 4's moving_average needed a loop. numpy-100's trick needs
# none: take np.cumsum of the prices, subtract the cumsum shifted by k,
# divide by k. Do it for the week's closes with k = 3, round to 2, and
# compare with session 4's answer [190.5, 188.7, 190.1, 191.7, 194.67].
# You should see:
#   Task 13: [190.5  188.7  190.1  191.7  194.67]

closes = np.array([190.5, 187.2, 193.8, 185.1, 191.4, 198.6, 194.0])
k = 3

# your code here


# ── ★ Task 14 · Maximum drawdown, vectorised ────────────────────────
# Session 4's max_drawdown kept the running peak in a loop.
# np.maximum.accumulate(a) gives the running maximum of an array in one
# call. Use it to compute the worst drawdown of the closes in one or two
# lines; print it as a percentage with 2 decimals. It must match session
# 4: -4.49%.
# You should see:
#   Task 14: -4.49%

closes = np.array([190.5, 187.2, 193.8, 185.1, 191.4, 198.6, 194.0])

# your code here
