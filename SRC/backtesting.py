def train_test_split(series, ratio=0.8):

    split = int(len(series) * ratio)

    train = series[:split]

    test = series[split:]

    return train, test