from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import numpy as np


def get_metrics(actual, pred):

    mae = mean_absolute_error(actual, pred)

    rmse = np.sqrt(
        mean_squared_error(actual, pred)
    )

    mape = (
        np.mean(
            np.abs(
                (np.array(actual) - np.array(pred))
                / np.array(actual)
            )
        ) * 100
    )

    return mae, rmse, mape


def mase(actual, pred, train):

    import numpy as np

    naive_err = np.abs(
        np.diff(train)
    ).mean()

    model_err = np.abs(
        np.array(actual)
        - np.array(pred)
    ).mean()

    return model_err / naive_err