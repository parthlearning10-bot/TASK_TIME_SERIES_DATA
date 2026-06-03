import pandas as pd
def error_drift(actual, pred):

    err = abs(actual - pred)

    return pd.Series(err)


import pandas as pd


def rolling_error(actual, pred, window=30):

    err = abs(actual - pred)

    err = pd.Series(err)

    return err.rolling(window).mean()