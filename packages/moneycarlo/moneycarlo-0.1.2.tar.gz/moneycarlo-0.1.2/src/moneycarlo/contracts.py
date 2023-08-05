from datetime import datetime
from random import choices


class Contract:
    def __init__(self, pwin: float, value: float, award_date: datetime) -> None:
        self.probability_of_win: float = pwin
        self.value: float = value
        self.award_date: datetime = award_date

    def predict_win(self, num_its: int) -> list[float]:
        return choices([self.value, 0.0], cum_weights=[self.probability_of_win, 1.0], k=num_its)

    @classmethod
    def from_csv_line(cls, line: str) -> "Contract":
        contents: list = line.split(",")
        year: int = int(contents[0])
        month: int = 3 * int(contents[1])
        pwin: float = 0.0
        if contents[2] == "low":
            pwin = 0.25
        elif contents[2] == "medium":
            pwin = 0.5
        elif contents[2] == "high":
            pwin = 0.75
        elif contents[2] == "won":
            pwin = 1.0

        val: float = float(contents[3])
        return cls(pwin, val, datetime(year, month, 1))


class RevenuePlan:
    def __init__(self) -> None:
        self.contracts: list[Contract] = []
        self.quarters: dict = {}

    @classmethod
    def from_csv(cls, contracts_csv_name: str) -> "RevenuePlan":

        plan: RevenuePlan = cls()

        with open(contracts_csv_name, "r") as f:
            lines = f.readlines()

        for line in lines[1:]:
            plan.add_contract(Contract.from_csv_line(line))

        return plan

    def add_contract(self, ct: Contract) -> None:
        self.contracts.append(ct)
        if self.quarters.get(ct.award_date) is None:
            self.quarters[ct.award_date] = 0

    def predict_revenue(self, num_its: int) -> list[float]:
        sims: list[float] = [0 for _ in range(num_its)]
        for ct in self.contracts:
            for i, val in enumerate(ct.predict_win(num_its)):
                sims[i] += val
        return sims
