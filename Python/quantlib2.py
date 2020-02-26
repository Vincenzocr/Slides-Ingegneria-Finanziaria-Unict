from QuantLib import *
import pandas as pd
from datetime import date
from matplotlib.dates import MonthLocator, DateFormatter
import matplotlib.pyplot as plt
from numpy import *


def to_datetime(d):
    return date(d.year(), d.month(), d.dayOfMonth())


def format_rate(r):
    return "%.4f %%" % (r.rate() * 100.0)


def plot_curve(*curves):
    fig, ax = plt.subplots()
    plt.rc("lines", linewidth=4)
    ax.set_color_cycle(["b", "y", "c", "k"])
    dates = [today + Period(i, Weeks) for i in range(0, 52 * 5)]
    for c in curves:
        valid_dates = [d for d in dates if d >= c.referenceDate()]
        rates = [c.forwardRate(d, d+1, Actual360(), Simple).rate() for d in valid_dates]
        ax.plot_date([to_datetime(d) for d in valid_dates], rates, '-')
    ax.set_xlim(to_datetime(min(dates)), to_datetime(max(dates)))
    ax.xaxis.set_major_locator(MonthLocator(bymonth=[6, 12]))
    ax.xaxis.set_major_formatter(DateFormatter('%b %y'))
    ax.set_ylim(0.001, 0.009)
    ax.autoscale_view()
    ax.xaxis.grid(True, "major")
    ax.xaxis.grid(False, "minor")
    fig.autofmt_xdate()
    plt.show()

today = Date(8, October, 2014)
Settings.instance().evaluationDate = today

helpers = [SwapRateHelper(QuoteHandle(SimpleQuote(rate/100.0)),
                          Period(*tenor), TARGET(),
                          Annual, Unadjusted,
                          Thirty360(),
                          Euribor6M())
           for tenor, rate in [((6, Months), 0.201),
                               ((2, Years), 0.258),
                               ((5, Years), 0.464),
                               ((10, Years), 0.151),
                               ((15, Years), 1.588)]]
curve = PiecewiseLinearZero(0, TARGET(), helpers, Actual360())
plot_curve(curve)

future_reference = today + Period(1, Years)
implied_curve = ImpliedTermStructure(YieldTermStructureHandle(curve), future_reference)
plot_curve(implied_curve)
plot_curve(curve, implied_curve)

df = pd.DataFrame([(T, format_rate(implied_curve.zeroRate(T, Continuous))) for T in range(6)],
                  columns=("Time", "Zero Rate"), index=[""]*6)
print(df)
# Settings.instance().evaluationDate = future_reference
#
# df1 = pd.DataFrame([(T, format_rate(implied_curve.zeroRate(T, Continuous))) for T in range(6)],
#                    columns=("Time", "Zero Rate"), index=[""]*6)
# print(df1)
# Settings.instance().evaluationDate = today + Period(3, Months)
# Settings.instance().evaluationDate = today + Period(1, Years)

print(curve.nodes())

dates, rates = zip(*curve.nodes())
frozen_curve = ZeroCurve(dates, rates, curve.dayCounter())
implied_curve = ImpliedTermStructure(YieldTermStructureHandle(frozen_curve),
                                     future_reference)
Settings.instance().evaluationDate = future_reference
plot_curve(frozen_curve)
plot_curve(implied_curve)
df3 = pd.DataFrame([(T, format_rate(frozen_curve.zeroRate(T, Continuous)),
                     format_rate(implied_curve.zeroRate(T, Continuous)))
                    for T in range(6)],
                   columns=("Time", "Zero Rate", "Implied Zero Rate"), index=[""]*6)
