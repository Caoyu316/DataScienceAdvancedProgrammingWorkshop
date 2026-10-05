# Session 2 exercises — values, names, types
#
# Work through the tasks in order. For every task that says PREDICT,
# write your prediction in the comment BEFORE you press ▷. Pressing ▷
# runs the whole file; each task prints its own label, so you can see
# which output belongs to which task. Write your own code under "your
# code here". Answers go into Wooclap.


# ════════════════════════════════════════════════════════════════════
# Read and debug
# ════════════════════════════════════════════════════════════════════

# ── Task 1 · PREDICT: names are labels, not formulas ────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 2 · DEBUG: the money disappeared ───────────────────────────
# Buying shares at the market price does not make you richer or poorer:
# shares × price + cash is the same before and after a purchase.
#
# This code runs without an error, but it breaks that rule. Find the
# line, say in one sentence what it does wrong, and fix it.
# First answer in Wooclap (which line?), then fix it here.

shares = 4
price = 102.3
cash = 1000.0
wealth_before = shares * price + cash

shares = shares + 6
cash = cash - shares * price

wealth_after = shares * price + cash
print("Task 2:", wealth_before, wealth_after)


# ── Task 3 · PREDICT: the clever swap ───────────────────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 4 · PREDICT: the default that eats a value ─────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.


# ── Task 5 · PREDICT: one fee, two roundings ────────────────────────
# In Wooclap, with a timer: read the code on the screen and answer
# without running anything.



# ════════════════════════════════════════════════════════════════════
# Write it yourself
# ════════════════════════════════════════════════════════════════════

# ── Task 6 · WRITE: a purchase with a rule ──────────────────────────
# You hold 2 VOO at 512.00 CHF and have 3000.00 CHF cash. Rule: spend at
# most 40 % of your cash, and buy whole shares only.
#
# Write the lines that work out how many shares you buy, update shares
# and cash, check that wealth did not change (with a tolerance, not ==),
# and print one line with an f-string.
# You should see:
#   VOO: bought 2, now 4 shares, cash 1976.00 CHF
#   True

ticker = "VOO"
shares = 2
price = 512.0
cash = 3000.0

# your code here


# ── Task 7 · WRITE: the same purchase in cents ──────────────────────
# Floats cannot store most prices exactly. Money is safer as whole
# cents. Redo Task 6 with integers only: 512.00 CHF is 51200 cents,
# 3000.00 CHF is 300000 cents.
#
# At the end, print the cash as CHF, built from // and % (no division,
# no float).
# You should see:
#   CHF 1976.00

shares = 2
price_c = 51200
cash_c = 300000

# your code here


# ── Task 8 · WRITE: the fee in cents, rounded half up ───────────────
# Back to Task 5's fee: 0.25 % of 1070.00 CHF. Compute it in cents with
# integers only, rounding half up (2.675 → 2.68), and print it as CHF
# with // and %.
#
# Hint: 1070.00 CHF is 107000 cents, and 0.25 % is 25 / 10000. Adding
# half of the divisor before // rounds half up.
# You should see:
#   fee CHF 2.68

trade_c = 107000

# your code here


# ── Task 9 · WRITE: split the cash to the last cent ─────────────────
# Split 1000.00 CHF between 3 accounts. Every account gets whole cents,
# and the three parts must add up to exactly 1000.00: no cent lost, no
# cent invented. Use cents, // and %. The first account takes the
# leftover cent.
#
# Then explain: why does round(1000.00 / 3, 2) * 3 not give 1000.00?
# You should see:
#   333.34 333.33 333.33
#   True
#   999.99

total_c = 100000

# your code here


# ── Task 10 · WRITE: swap two prices ────────────────────────────────
# The two lines below try to swap the prices. Run them. What went wrong,
# and why (think of Task 1)? Fix it so that the print shows 102.3 190.5.
# You should see:
#   Task 10: 102.3 190.5

price_a = 190.5
price_b = 102.3
price_a = price_b
price_b = price_a
print("Task 10:", price_a, price_b)



# ════════════════════════════════════════════════════════════════════
# ★ Harder: classic puzzles
# ════════════════════════════════════════════════════════════════════

# ── ★ Task 11 · Seconds to a clock time ─────────────────────────────
# A trade is stamped with the number of seconds since midnight: 34567.
# Print it as HH:MM:SS, with two digits each. Use // and % only.
# You should see:
#   09:36:07

t = 34567

# your code here


# ── ★ Task 12 · Reverse a 4-digit number ────────────────────────────
# Reverse the digits of a 4-digit account number using // and % only (no
# strings): 1234 becomes 4321. Test it on 1234 and on 5071. What happens
# to the 0 in 5071, and why?
# You should see:
#   1234 -> 4321
#   5071 -> 1705

n = 1234

# your code here


# ── ★ Task 13 · Leap years in one expression ────────────────────────
# Bond interest counts 366 days in a leap year. A year is a leap year if
# it divides by 4, except years that divide by 100, except again years
# that divide by 400.
#
# Write ONE boolean expression with and / or / not / % and print it for
# 2024, 2100, 2000 and 2026.
# You should see:
#   2024 True
#   2100 False
#   2000 True
#   2026 False

year = 2024

# your code here
