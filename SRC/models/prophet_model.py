from prophet import Prophet


def train_model(train_df):

    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False
    )

    model.fit(train_df)

    return model


def forecast(model, horizon):

    future = model.make_future_dataframe(
        periods=horizon,
        freq="D"
    )

    pred = model.predict(future)

    return pred