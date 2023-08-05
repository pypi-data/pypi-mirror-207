import unittest

from src.moneycarlo.contracts import Contract, RevenuePlan


class TestContract(unittest.TestCase):
    def test_from_csv_line(self):
        ct = Contract.from_csv_line("2023,1,low,1000")
        self.assertEqual(ct.probability_of_win, 0.25)
        self.assertEqual(ct.value, 1000.0)
        self.assertEqual(ct.award_date.year, 2023)
        self.assertEqual(ct.award_date.month, 3)
        self.assertEqual(ct.award_date.day, 1)


class TestRevenuePlan(unittest.TestCase):
    def test_from_csv(self):
        plan = RevenuePlan.from_csv("./tests/example_revenue_plan.csv")
        self.assertEqual(plan.contracts[0].probability_of_win, 1.0)
        self.assertEqual(plan.contracts[0].value, 1000.0)
        self.assertEqual(plan.contracts[0].award_date.year, 2023)
        self.assertEqual(plan.contracts[0].award_date.month, 3)
        self.assertEqual(plan.contracts[0].award_date.day, 1)
        self.assertEqual(plan.contracts[1].probability_of_win, 0.25)
        self.assertEqual(plan.contracts[1].value, 2000.0)
        self.assertEqual(plan.contracts[1].award_date.year, 2023)
        self.assertEqual(plan.contracts[1].award_date.month, 6)
        self.assertEqual(plan.contracts[1].award_date.day, 1)
        self.assertEqual(plan.contracts[2].probability_of_win, 0.5)
        self.assertEqual(plan.contracts[2].value, 3000.0)
        self.assertEqual(plan.contracts[2].award_date.year, 2023)
        self.assertEqual(plan.contracts[2].award_date.month, 9)
        self.assertEqual(plan.contracts[2].award_date.day, 1)
        self.assertEqual(plan.contracts[3].probability_of_win, 0.75)
        self.assertEqual(plan.contracts[3].value, 4000.0)
        self.assertEqual(plan.contracts[3].award_date.year, 2023)
        self.assertEqual(plan.contracts[3].award_date.month, 12)
        self.assertEqual(plan.contracts[3].award_date.day, 1)
