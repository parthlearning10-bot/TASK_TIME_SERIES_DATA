def forecast(train, test, lag=7):

    pred = []

    hist = list(train)

    for y in test:

        f = hist[-lag]

        pred.append(f)

        hist.append(y)

    return pred