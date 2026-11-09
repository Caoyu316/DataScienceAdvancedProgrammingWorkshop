# ═══════════════════════════════════════════════════════════════════
#  Session 9 workshop: how much does each share follow the market?
#
#  How it works:
#    1. Find the first ___ (three underscores) and replace it.
#    2. Press ▷ to run the whole file.
#    3. Read the result in the terminal:  ✓ = right,  ✗ = not yet (with a hint).
#    4. Pictures are saved as step-N.png next to this file:
#       open them in the Explorer on the left.
#  Then go to the next ___ . The steps build on each other: do them in order.
# ═══════════════════════════════════════════════════════════════════

# ── Setup: do not change anything until "Step 1" ───────────────────
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")                 # draw into files, not windows
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

HERE = Path(__file__).parent          # the folder this file is in
___ = None                            # the blanks you have not filled yet

# Pavel's make_prices.py: one year of SIMULATED daily prices, same every run.
rng = np.random.default_rng(2026)
days = pd.bdate_range(end="2026-10-30", periods=250)
market = rng.normal(0.0004, 0.0095, len(days))
_r = pd.DataFrame(index=days)
_r["AAPL"] = 0.0003 + 1.25 * market + rng.normal(0, 0.011, len(days))
_r["NESN"] = 0.0001 + 0.55 * market + rng.normal(0, 0.008, len(days))
_r["VOO"] = market
_r["MSFT"] = 0.0002 + 1.10 * market + rng.normal(0, 0.010, len(days))
_r.iloc[0] = 0.0
_p = ((1 + _r).cumprod())
_p = (_p / _p.iloc[-1] * pd.Series({"AAPL": 190.50, "NESN": 102.30, "VOO": 512.00, "MSFT": 410.00})).round(2)
_p.index.name = "Date"
_p.to_csv(HERE / "prices.csv")
_p.loc["2026-03-16", "AAPL"] = round(_p.loc["2026-03-16", "AAPL"] / 10, 2)   # one typo
_p.to_csv(HERE / "prices_typo.csv")

def check(n, got, want, hint, means=""):
    """Prints ✓ and what the result means, or ✗ and a hint, for step n."""
    try:
        ok = got == want if isinstance(want, (str, tuple)) else abs(float(got) - want) < 0.0015
    except (TypeError, ValueError):
        ok = False
    if ok:
        print(f"✓ Step {n}: right, {got}")
        if means:
            print(f"  → {means}")
    else:
        print(f"✗ Step {n}: not yet. {hint}")

def stuck(n, error):
    """Explains why step n stopped: a blank left, an earlier step, or Python's own message."""
    import re
    block = re.split(r"── (?:★ )?Step \d+:", Path(__file__).read_text(encoding="utf-8"))[n]
    if "___" in block:
        print(f"✗ Step {n}: fill the ___ in this step.")
    elif isinstance(error, NameError):
        print(f"✗ Step {n}: finish the steps before this one first ({error}).")
    else:
        print(f"✗ Step {n}: Python says {type(error).__name__}: {error}")
# ───────────────────────────────────────────────────────────────────


# ── Step 1: load the file and take a first look ────────────────────
# read_csv reads a table. Date becomes the index (the row labels).
try:
    prices = pd.___(HERE / "prices.csv", index_col="Date", parse_dates=True)
    print(prices.head(3))
    check(1, prices.shape, (250, 4), "Which pandas function READS a CSV file?",
          "250 days, 4 shares. Date is the index (the row labels), so it is not a column.")
except Exception as e:
    stuck(1, e)


# ── Step 2: daily returns, and which share moves the most ─────────
# pct_change() = (today - yesterday) / yesterday. The first day has no
# yesterday (NaN): dropna() removes it. describe() summarises every column.
try:
    returns = prices.pct_change().___() * 100        # in %
    print(returns.describe().round(2))
    check(2, returns.std().idxmax(), "AAPL", "Remove the first row: which method drops the NaN rows?",
          "Apple moves about 1.7 % on a typical day, Nestlé only 0.9 %. Read the std row above.")
except Exception as e:
    stuck(2, e)


# ── Step 3: PICTURE — the year, all four shares start at 100 ─────────
# Divide every row by the FIRST row, times 100. Open step-3.png.
try:
    growth = prices / prices.iloc[___] * 100
    growth.plot(figsize=(8, 4), title="Growth of 100")
    plt.savefig(HERE / "step-3.png")
    plt.close()
    check(3, round(growth.iloc[-1]["AAPL"], 1), 142.0, "Which row is the first one? (positions start at...)",
          "100 francs in Apple became 142. In step-3.png: the four lines go up and down on the SAME days.")
except Exception as e:
    stuck(3, e)


# ── Step 4: PICTURE — the cloud: market (x) against Apple (y) ─────────
# Nothing to fill: run it, open step-4.png, and GUESS the slope.
try:
    plt.figure(figsize=(5, 5))
    plt.scatter(returns["VOO"], returns["AAPL"], s=10)
    plt.xlabel("VOO (the market), daily return %")
    plt.ylabel("AAPL, daily return %")
    plt.savefig(HERE / "step-4.png")
    plt.close()
    check(4, round(returns["AAPL"].corr(returns["VOO"]), 3), 0.759, "Run steps 1 and 2 first.",
          "Correlation 0.76: the cloud in step-4.png rises, and fairly tightly. Guess the slope before step 5!")
except Exception as e:
    stuck(4, e)


# ── Step 5: the line with scikit-learn: make a model, FIT it, read it ──
# X must be a TABLE (double brackets), y one column.
try:
    X = returns[["VOO"]]
    y = returns["AAPL"]
    model = LinearRegression().___(X, y)
    beta = model.coef_[0]
    print("beta:", round(beta, 3), " R²:", round(model.score(X, y), 3))
    check(5, round(beta, 3), 1.296, "The scikit-learn verb that learns from the data: model.___(X, y)",
          "When the market moves 1 %, Apple moves 1.3 % on average. Same number as cov / var in the lecture.")
except Exception as e:
    stuck(5, e)


# ── Step 6: PICTURE — the line on the cloud, and a forecast ───────────
# predict() gives the point on the line. The market falls 2 % tomorrow:
# what does the line say for Apple? Open step-6.png.
try:
    plt.figure(figsize=(5, 5))
    plt.scatter(returns["VOO"], returns["AAPL"], s=10)
    plt.plot(returns["VOO"], model.predict(X), color="red")
    plt.savefig(HERE / "step-6.png")
    plt.close()
    tomorrow = pd.DataFrame({"VOO": [___]})
    forecast = model.predict(tomorrow)[0]
    check(6, round(forecast, 2), -2.58, "The market FALLS by 2 %: which number goes in the table?",
          "The line says Apple falls 2.6 %. ON AVERAGE: in step-6.png, single days are far from the red line.")
except Exception as e:
    stuck(6, e)


# ── Step 7: PICTURE — one typo in the file ────────────────────────────
# prices_typo.csv has ONE Apple price with the decimal point moved.
# Fit the same line on it. Look at the beta, at describe(), at step-7.png.
try:
    bad = pd.read_csv(HERE / ___, index_col="Date", parse_dates=True)
    rb = bad.pct_change().dropna() * 100
    m_bad = LinearRegression().fit(rb[["VOO"]], rb["AAPL"])
    print("beta with the typo:", round(m_bad.coef_[0], 3))
    print(rb["AAPL"].describe().round(1))
    plt.figure(figsize=(5, 5))
    plt.scatter(rb["VOO"], rb["AAPL"], s=10)
    plt.savefig(HERE / "step-7.png")
    plt.close()
    check(7, rb["AAPL"].idxmin().strftime("%Y-%m-%d"), "2026-03-16", "Which FILE has the typo? Give its name as text.",
          "ONE wrong price out of 250 turned the beta from +1.3 into -0.75. describe() shows it: min -90 %, max +900 %.")
except Exception as e:
    stuck(7, e)


# ═══ Part 2: build it yourself, no scikit-learn ══════════════════
#  This morning Pavel built the line by hand. Now you do it, and you
#  check that you get EXACTLY the numbers scikit-learn gave you.

# ── Step 8: the slope by hand ─────────────────────────────────────────
# Least squares: b = sum(dx * dy) / sum(dx * dx), where dx and dy are the
# distances from the mean. Then the line goes through the two means.
try:
    x = returns["VOO"]
    y = returns["AAPL"]
    dx = x - x.mean()
    dy = y - y.___
    b = (dx * dy).sum() / (dx * dx).sum()
    a = y.mean() - b * x.mean()
    print("by hand: a =", round(a, 3), " b =", round(b, 3))
    check(8, round(b, 3), 1.296, "dy is the distance of y from ITS mean: y - y.___",
          "Exactly the beta of step 5. scikit-learn's fit is just this formula.")
except Exception as e:
    stuck(8, e)


# ── Step 9: R² by hand ────────────────────────────────────────────────
# R² = 1 - (what the line misses) / (all the movement of y).
# Both are sums of SQUARED distances.
try:
    fitted = a + b * x                  # the point on the line, every day
    residuals = y - fitted              # what the line misses
    r2 = 1 - (residuals ** 2).sum() / (dy ** ___).sum()
    check(9, round(r2, 3), 0.577, "Squared distances: dy to the power ___",
          "The market explains 58 % of Apple's daily moves. The other 42 % (the residuals) is Apple's own news.")
except Exception as e:
    stuck(9, e)


# ── Step 10: PICTURE — the computer finds the line by walking downhill ──
# Gradient descent, as in the lecture: start from a flat line (a = b = 0),
# measure the error, take a small step in the direction that LOWERS it,
# repeat. Open step-10.png: the error at every step.
try:
    a_gd, b_gd = 0.0, 0.0
    rate = 0.1                          # the size of each step
    losses = []
    for step in range(60):
        errors = (a_gd + b_gd * x) - y
        losses.append((errors ** 2).mean())
        grad_a = 2 * errors.mean()
        grad_b = 2 * (errors * x).mean()
        a_gd = a_gd - rate * grad_a     # a step DOWNHILL
        b_gd = ___    # the same step for b: copy the line above
    plt.figure(figsize=(6, 3))
    plt.plot(losses)
    plt.xlabel("step")
    plt.ylabel("mean squared error")
    plt.savefig(HERE / "step-10.png")
    plt.close()
    print("after 60 steps: a =", round(a_gd, 3), " b =", round(b_gd, 3))
    check(10, round(b_gd, 3), 1.296, "Write the step for b like the step for a, one line above.",
          "60 small steps reach the same line again. The error falls fast, then flattens: see step-10.png.")
except Exception as e:
    stuck(10, e)


# ═══ ★ Faster? Three more steps ═══════════════════════════════════


# ── ★ Step 11: every position has a beta ──────────────────────────────
# Same fit in a for loop. Which share follows the market least?
try:
    for ticker in ["AAPL", "NESN", "MSFT"]:
        m = LinearRegression().fit(returns[["VOO"]], returns[___])
        print(ticker, "beta", round(m.coef_[0], 3), "R²", round(m.score(returns[["VOO"]], returns[ticker]), 3))
    check(11, round(m.coef_[0], 3), 1.113, "y is the column of the share in the loop: returns[___]",
          "Nestlé: beta 0.47, R² 0.26. It follows the market least: people buy food in every economy.")
except Exception as e:
    stuck(11, e)


# ── ★ Step 12: a beta is an estimate, not a fixed number ─────────────
# Fit Apple's line on the first half of the year, then on the second half.
try:
    first = returns.iloc[:125]
    second = returns.iloc[___]
    b1 = LinearRegression().fit(first[["VOO"]], first["AAPL"]).coef_[0]
    b2 = LinearRegression().fit(second[["VOO"]], second["AAPL"]).coef_[0]
    print("first half:", round(b1, 3), " second half:", round(b2, 3))
    check(12, round(b2, 3), 1.348, "The second half starts at row 125 and goes to the end: [___]",
          "1.23 and 1.35 from the SAME share: with other days, another number. Every estimate from data has noise.")
except Exception as e:
    stuck(12, e)


# ── ★ Step 13: the beta of the whole ledger ───────────────────────────
# Weight of a position = its value / the total value.
# Portfolio beta = sum of weight × beta. VOO's beta is 1: it IS the market.
try:
    value = pd.Series({"AAPL": 10 * 190.50, "NESN": 4 * 102.30, "VOO": 2 * 512.00})
    weight = value / value.___
    betas = pd.Series({"AAPL": 1.296, "NESN": 0.474, "VOO": 1.0})
    b_port = (weight * betas).sum()
    print("weights:", weight.round(3).to_dict())
    check(13, round(b_port, 3), 1.104, "The total value of the ledger: value.___",
          "Beta 1.1: if the market falls 2 %, the ledger falls about 2.2 %. Apple is 57 % of it.")
except Exception as e:
    stuck(13, e)
