MODEL_PATH = r"C:\Users\com125\Desktop\Parth_Intern\SRC\models\xgb_model.pkl"

DATA_PATH = r"C:\Users\com125\Desktop\Parth_Intern\DATA\births_clean.csv"


def get_forecast(horizon):

    model = joblib.load(MODEL_PATH)

    df = pd.read_csv(DATA_PATH)

    df["date"] = pd.to_datetime(df["date"])

    vals = df["births"].tolist()

    preds = []

    for step in range(horizon):

        last_date = df["date"].iloc[-1]

        next_date = last_date + pd.Timedelta(days=step + 1)

        row = pd.DataFrame({
            "lag1": [vals[-1]],
            "lag7": [vals[-7]],
            "lag14": [vals[-14]],
            "lag30": [vals[-30]],
            "dow": [next_date.dayofweek],
            "month": [next_date.month]
        })
        # business drift logic building now for that what

        pred = model.predict(row)[0]

        pred = round(float(pred), 2)

        preds.append(pred)

        vals.append(pred)

    return preds