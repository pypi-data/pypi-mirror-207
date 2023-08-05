import sys
from statistics import median

from moneycarlo.contracts import RevenuePlan

if __name__ == "__main__":
    pred = RevenuePlan.from_csv(sys.argv[1]).predict_revenue(int(sys.argv[2]))
    print(min(pred), median(pred), max(pred))
