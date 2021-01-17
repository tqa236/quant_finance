import unittest

from forward import spot_rate, forward_rate, fix_leg_forward


class Test(unittest.TestCase):
    def test_1(self):
        bond_prices = [0.9891, 0.9688, 0.9423]
        forward_rates = [0.011020, 0.015975, 0.020008]
        for i in range(len(bond_prices)):
            self.assertAlmostEqual(
                spot_rate(bond_prices[i], i + 1), forward_rates[i], 4
            )

        self.assertAlmostEqual(
            forward_rate(forward_rates[0], 1, forward_rates[1], 2), 0.0209542, 4
        )

    def test_2(self):
        float_legs = [38.5, 43.4, 46.1]
        periods = [1 / 12, 2 / 12, 3 / 12]
        rate = 2.4 / 100
        self.assertAlmostEqual(fix_leg_forward(float_legs, periods, rate), 42.6616, 4)


if __name__ == "__main__":
    unittest.main()