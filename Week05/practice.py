# Session 5 extra practice — classics. Optional and ungraded; nothing is
# handed in. Solutions follow a week later.

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
# Extra practice: classics (optional, ungraded)
# ════════════════════════════════════════════════════════════════════

# ── Practice 1 · apply or np.where ──────────────────────────────────
# Label each row of df "large" if its value is above 1500, otherwise
# "small", twice: once with .apply and a lambda (as in the lecture),
# once with np.where. Check that both give the same list.
# You should see:
#   ['large', 'small', 'small', 'small'] True

# your code here


# ── Practice 2 · Positions never traded (LeetCode pandas: customers who never order) ────
# Today's trades were only in AAPL and VOO. Which positions of df were
# not traded? Use .isin() and ~ (not, element by element).
# You should see:
#   ['MSFT', 'NESN']

traded = ["AAPL", "VOO"]

# your code here


# ── Practice 3 · Compound the daily returns ─────────────────────────
# From the week's closes, compute the daily returns (two shifted
# slices), then compound them with np.cumprod(1 + returns). Show that
# the last value equals last price / first price, and print the week's
# return in percent.
# You should see:
#   1.018373 1.018373 1.84

closes = np.array([190.5, 187.2, 193.8, 185.1, 191.4, 198.6, 194.0])

# your code here
