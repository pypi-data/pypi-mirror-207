import sys

from moneycarlo.contracts import RevenuePlan

if __name__ == "__main__":
    print(RevenuePlan.from_csv(sys.argv[1]).predict_revenue(int(sys.argv[2])))
