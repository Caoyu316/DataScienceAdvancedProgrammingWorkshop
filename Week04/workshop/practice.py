# Session 4 extra practice — classics. Optional and ungraded; nothing is
# handed in. Solutions follow a week later.

closes = [190.5, 187.2, 193.8, 185.1, 191.4, 198.6, 194.0]   # AAPL, day 0 to day 6


# ════════════════════════════════════════════════════════════════════
# Extra practice: classics (optional, ungraded)
# ════════════════════════════════════════════════════════════════════

# ── Practice 1 · Binary search ──────────────────────────────────────
# Write binary_search(xs, target) for a SORTED list: look at the middle
# item; if it is too small, keep only the right half, if too big, the
# left half; repeat until found. Return the position, or -1 if the
# target is not there. Test it on the prices below with 410.0 and with
# 100.0.
# You should see:
#   3 -1

prices = [88.7, 102.3, 190.5, 410.0, 512.0]

# your code here


# ── Practice 2 · Write your own sort ────────────────────────────────
# Write bubble_sort(xs) that returns a NEW sorted list and leaves xs
# unchanged: walk through the list, swap every neighbour pair that is in
# the wrong order, and repeat until nothing is out of order. Print the
# result and the original list.
# You should see:
#   [88.7, 102.3, 190.5, 410.0, 512.0] [512.0, 102.3, 410.0, 88.7, 190.5]

unsorted = [512.0, 102.3, 410.0, 88.7, 190.5]

# your code here


# ── Practice 3 · Euclid: identical baskets ──────────────────────────
# You want to split 8 AAPL and 12 NESN shares into identical baskets, as
# many baskets as possible, each with the same number of AAPL and of
# NESN. That number of baskets is the greatest common divisor. Write
# gcd(a, b) with Euclid's rule: replace (a, b) by (b, a % b) until b is
# 0; then a is the answer. Print gcd(8, 12), gcd(10, 4) and gcd(9, 4).
# You should see:
#   4 2 1

# your code here
