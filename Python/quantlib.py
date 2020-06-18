from QuantLib import *
import matplotlib.pyplot as plot
import numpy as np

today = Date(7, March, 2014)
Settings.instance().evaluationDate = today
option = EuropeanOption(PlainVanillaPayoff(Option.Call, 100.0), EuropeanExercise(Date(7, June, 2014)))

u = SimpleQuote(100.0)
r = SimpleQuote(0.01)
sigma = SimpleQuote(0.2)

riskFreeCurve = FlatForward(0, TARGET(), QuoteHandle(r), Actual360())
volatility = BlackConstantVol(0, TARGET(), QuoteHandle(sigma), Actual360())

process = BlackScholesProcess(QuoteHandle(u), YieldTermStructureHandle(riskFreeCurve), BlackVolTermStructureHandle(volatility))

engine = AnalyticEuropeanEngine(process)

option.setPricingEngine(engine)

print(option.NPV())
print(option.delta())
print(option.gamma())
print(option.vega())

u.setValue(105.00)
print(option.NPV())

f, ax = plot.subplots()
xs = np.linspace(80.00, 120.0, 400)
ys = []


Settings.instance().evaluationDate = Date(7, April, 2014)
print(option.NPV())
Settings.instance().evaluationDate = Date(7, May, 2014)
print(option.NPV())
Settings.instance().evaluationDate = Date(17, May, 2014)
print(option.NPV())
Settings.instance().evaluationDate = Date(27, May, 2014)
print(option.NPV())
Settings.instance().evaluationDate = Date(6, June, 2014)
print(option.NPV())

for x in xs:
    u.setValue(x)
    ys.append(option.NPV())

ax.set_title("Option Value")
_ = ax.plot(xs, ys)
plot.show()

model = HestonModel(
    HestonProcess(YieldTermStructureHandle(riskFreeCurve),
                  YieldTermStructureHandle(FlatForward(0, TARGET(), 0.0, Actual360())),
                  QuoteHandle(u),
                  0.004, 0.1, 0.01, 0.05, -0.75))
engine = AnalyticHestonEngine(model)
option.setPricingEngine(engine)
print(option.NPV())

engine = MCEuropeanEngine(process, "PseudoRandom",
                          timeSteps=20,
                          requiredSamples=2500)
option.setPricingEngine(engine)
print(option.NPV())
