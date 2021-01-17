import numpy as np


def calculate_present_value(amount, rate, period):
    """Present value for the continous compounding interest rate."""
    return amount * np.exp(-rate * period)


def spot_rate(bond_price, year):
    return (1 / bond_price) ** (1 / year) - 1


def forward_rate(spot_rate1, year1, spot_rate2, year2):
    return ((1 + spot_rate2) ** year2 / (1 + spot_rate1) ** year1) ** (
        year2 - year1
    ) - 1


def fix_leg_forward(float_legs, periods, rate):
    present_value = 0
    for float_leg, period in zip(float_legs, periods):
        present_value += calculate_present_value(float_leg, rate, period)
    fix_legs = [1] * len(periods)
    fix_leg_values = sum(
        calculate_present_value(fix_leg, rate, period)
        for fix_leg, period in zip(fix_legs, periods)
    )
    return present_value / fix_leg_values
