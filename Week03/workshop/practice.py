# Session 3 extra practice — classics. Optional and ungraded; nothing is
# handed in. Solutions follow a week later.

tickers = ["AAPL", "NESN", "VOO"]
shares = [10, 4, 2]
price = {"AAPL": 190.5, "NESN": 102.3, "VOO": 512.0}
closes = [190.5, 187.2, 193.8, 185.1, 191.4, 198.6, 194.0]   # AAPL, day 0 to day 6


# ════════════════════════════════════════════════════════════════════
# Extra practice: classics (optional, ungraded)
# ════════════════════════════════════════════════════════════════════

# ── Practice 1 · The second-highest close, in one pass ──────────────
# Find the highest and the second-highest close of the week in ONE loop,
# without sorted() or max(). Keep two names, best and second, and decide
# for each price which one it replaces.
# You should see:
#   198.6 194.0

# your code here


# ── Practice 2 · Remove duplicates, keep the order ──────────────────
# Build a new list with each ticker once, in the order it FIRST
# appeared. Use a dict to remember what you have seen.
# You should see:
#   ['AAPL', 'NESN', 'VOO', 'MSFT']

trades = ["AAPL", "NESN", "VOO", "NESN", "AAPL", "MSFT"]

# your code here


# ── Practice 3 · The longest rising streak ──────────────────────────
# A rising streak is a run of days where each close is higher than the
# day before. How many days long is the longest streak in closes (a
# single day counts as a streak of 1)?
# You should see:
#   3

# your code here


# ── Practice 4 · Merge two holdings ─────────────────────────────────
# Two accounts hold shares: a = {"AAPL": 10, "NESN": 4} and b = {"NESN":
# 6, "VOO": 2}. Build ONE dict with the total shares per ticker, and
# leave a unchanged (check it at the end).
# You should see:
#   {'AAPL': 10, 'NESN': 10, 'VOO': 2} {'AAPL': 10, 'NESN': 4}

a = {"AAPL": 10, "NESN": 4}
b = {"NESN": 6, "VOO": 2}

# your code here
