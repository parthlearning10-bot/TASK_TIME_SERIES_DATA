import pandas as pd


def error_drift(actual, pred):

    err = abs(actual - pred)

    return pd.Series(err)