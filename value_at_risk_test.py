import unittest

from value_at_risk import value_at_risk, var_to_std


class Test(unittest.TestCase):
    def test_1(self):
        portfolio_value = 2 * 10 ** 6
        std = 1.8 / 100
        confidence_level = 0.95
        self.assertEqual(
            value_at_risk(portfolio_value, std, confidence_level), 59214.730570253014
        )

    def test_2(self):
        portfolio_value = 5 * 10 ** 6
        var = 45000
        confidence_level = 0.95
        self.assertEqual(
            var_to_std(portfolio_value, var, confidence_level), 0.005471611487205922
        )


if __name__ == "__main__":
    unittest.main()