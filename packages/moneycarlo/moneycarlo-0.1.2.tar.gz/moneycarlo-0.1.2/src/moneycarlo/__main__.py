import sys
from statistics import mode

from moneycarlo.contracts import RevenuePlan

if __name__ == "__main__":
    its = int(sys.argv[2])
    pred = RevenuePlan.from_csv(sys.argv[1]).predict_revenue(its)
    low = min(pred)
    high = max(pred)
    best = mode(pred)
    plow = pred.count(low) / its * 100
    phigh = pred.count(high) / its * 100
    pbest = pred.count(best) / its * 100
    print("Low:    ${:12.2f} with {:6.2f}% occurrence".format(low, plow))
    print("High:   ${:12.2f} with {:6.2f}% occurrence".format(high, phigh))
    print("Mode:   ${:12.2f} with {:6.2f}% occurrence".format(best, pbest))
