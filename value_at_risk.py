import scipy.stats as st


def value_at_risk(portfolio_value, std, confidence_level=0.95):
    z_score = st.norm.ppf(confidence_level)
    return portfolio_value * std * z_score


def var_to_std(portfolio_value, var, confidence_level=0.95):
    z_score = st.norm.ppf(confidence_level)
    return var / (portfolio_value * z_score)
