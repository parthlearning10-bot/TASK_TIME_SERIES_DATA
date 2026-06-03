from fastapi import FastAPI
import sys

sys.path.append(
    r"C:\Users\com125\Desktop\Parth_Intern\SRC"
)

from forecast_service import get_forecast
from logger import logger


app = FastAPI(
    title="US Birth Forecast API",
    description="Forecast future US Birth counts using trained XGBoost model",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message": "US Birth Forecast API Running"
    }


@app.get("/forecast")
def forecast(horizon: int = 7):

    try:

        logger.info(
            f"Forecast request received. Horizon={horizon}"
        )

        if horizon <= 0:
            raise ValueError(
                "Horizon must be greater than 0"
            )

        fcst = get_forecast(horizon)

        lower = [
            round(x - 418.53, 2)
            for x in fcst
        ]

        upper = [
            round(x + 418.53, 2)
            for x in fcst
        ]

        return {
            "horizon": horizon,
            "forecast": fcst,
            "confidence_interval": {
                "lower": lower,
                "upper": upper
            },
            "recent_metrics": {
                "mae": 282.22,
                "rmse": 418.53,
                "mape": 2.69,
                "mase": 0.441
            }
        }

    except Exception as e:

        logger.error(
            f"Forecast error: {str(e)}"
        )

        return {
            "error": str(e)
        }