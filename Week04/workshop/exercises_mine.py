# Session 4 exercises — functions, methods, modules, classes
#
# PREDICT means write your prediction in the comment before you press ▷.
# Each task prints its own label. Write your own code under "your code
# here". From today, most answers are FUNCTIONS: write the def, then
# call it with the values given and print what it returns.

closes = [190.5, 187.2, 193.8, 185.1, 191.4, 198.6, 194.0]   # AAPL, day 0 to day 6


# ════════════════════════════════════════════════════════════════════
# Read and debug
# ════════════════════════════════════════════════════════════════════

# ── Task 1 · PREDICT: print is not return ───────────────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 2 · PREDICT: two variables called total ────────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 3 · PREDICT: what the function changed ─────────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 4 · PREDICT: which methods change the value? ───────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 5 · DEBUG: the weight that lies ────────────────────────────
# AAPL is worth 1905.0 of a 3338.2 CHF ledger. The function below
# computes its weight in percent. The call runs and prints a number. Is
# it right? Find the mistake and fix it so that no one can make it
# again.
# First answer in Wooclap (which line?), then fix it here.

def weight(value, total):
    return value / total * 100

print("Task 5:", f"{weight(3338.2, 1905.0):.1f}%")

a = weight(1905.0, 3338.2)
print("Task 5:", f"{a:.1f}%")




# ════════════════════════════════════════════════════════════════════
# Write it yourself
# ════════════════════════════════════════════════════════════════════

# ── Task 6 · WRITE: two functions for the ledger ────────────────────
# The ledger is a list of (ticker, shares, price) tuples. Write
# position_value(shares, price) that returns the value of one position,
# and total_value(positions) that loops over the tuples, unpacks each
# one, and returns the sum of position_value for all of them. Both need
# a one-line docstring. Print total_value(ledger).
# You should see:
#   Task 6: 3338.2

ledger = [("AAPL", 10, 190.5), ("NESN", 4, 102.3), ("VOO", 2, 512.0)]

# your code here


# ── Task 7 · WRITE: a fee with defaults ─────────────────────────────
# Write fee(value, rate=0.001, minimum=5.0) that returns value × rate,
# but never less than minimum. Then print, on one line, fee(1000.0),
# fee(10000.0) and fee(10000.0, rate=0.002).
# You should see:
#   Task 7: 5.0 10.0 20.0

# your code here


# ── Task 8 · WRITE: session 3's while, as a function ────────────────
# Write years_to_reach(start, target, rate=0.05) that returns how many
# whole years start needs to grow to at least target. Use while inside.
# Print years_to_reach(1000.0, 1500.0) and years_to_reach(1000.0,
# 1500.0, rate=0.03).
# You should see:
#   Task 8: 9 14

# your code here


# ── Task 9 · WRITE: teach Position a new method ─────────────────────
# Here is Pavel's Position class. Add a method buy(self, n) that
# increases the shares of THIS position by n. Then create aapl =
# Position("AAPL", 10, 190.5), call aapl.buy(5), and print aapl.shares
# and aapl.value().
# You should see:
#   Task 9: 15 2857.5

class Position:
    """One position: a ticker, a number of shares, a price."""

    def __init__(self, ticker, shares, price):
        self.ticker = ticker
        self.shares = shares
        self.price = price

    def value(self):
        return self.shares * self.price

    # your method here

# your code here


# ── Task 10 · WRITE: a module instead of a loop ─────────────────────
# import the standard-library module statistics. Print the mean (rounded
# to 2 decimals), the median and the standard deviation (rounded to 2)
# of the week's closes. Look up the function names with help(statistics)
# or by typing statistics. and waiting.
# You should see:
#   Task 10: 191.51 191.4 4.52

# your code here



# ════════════════════════════════════════════════════════════════════
# ★ Harder: classic puzzles
# ════════════════════════════════════════════════════════════════════

# ── ★ Task 11 · Moving average ──────────────────────────────────────
# Write moving_average(prices, k) that returns a list: the average of
# every run of k days in a row, each rounded to 2 decimals. Use a slice
# for each window. Print moving_average(closes, 3).
# You should see:
#   Task 11: [190.5, 188.7, 190.1, 191.7, 194.67]

# your code here


# ── ★ Task 12 · Net positions from a list of trades ─────────────────
# Trades arrive as (ticker, quantity) tuples; a negative quantity is a
# sale. Write net_positions(trades) that returns a dict: ticker → shares
# held after all trades. Print it for the trades below.
# You should see:
#   Task 12: {'AAPL': 7, 'NESN': 0, 'VOO': 2}

trades = [("AAPL", 10), ("NESN", 4), ("AAPL", -3), ("VOO", 2), ("NESN", -4)]

# your code here


# ── ★ Task 13 · Merge two sorted lists ──────────────────────────────
# Two traders logged their trade times (HHMM as whole numbers), each
# list already sorted. Write merge_sorted(a, b) that returns one sorted
# list WITHOUT sorted() or .sort(): walk through both lists with two
# positions and always take the smaller front item.
# You should see:
#   Task 13: [930, 945, 1015, 1015, 1200, 1340, 1555]

times_a = [930, 1015, 1340, 1555]
times_b = [945, 1015, 1200]

# your code here


# ── ★ Task 14 · Maximum drawdown ────────────────────────────────────
# The drawdown on a day is how far the price is below the highest price
# seen so far, in percent. Write max_drawdown(prices) that returns the
# worst drawdown of the period (a negative number). Print it for closes
# as a percentage with 2 decimals.
# You should see:
#   Task 14: -4.49%

# your code here
