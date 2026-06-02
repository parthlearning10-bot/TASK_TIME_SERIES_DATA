def forecast(train, test):

    pred = []

    hist = list(train)

    for y in test:

        f = hist[-1]

        pred.append(f)

        hist.append(y)

    return pred