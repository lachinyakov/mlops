import numpy as np


def generator(data, lookback, delay, min_index, max_index, shuffle=False, batch_size=128, step=6):
    i = 0
    if max_index is None:
        max_index = len(data) - delay - 1
        i = min_index + lookback
    while 1:
        if shuffle:
            # batch_size рандомных чисел в диапазоне от мин-й точки отсчета до максимума
            rows = np.random.randint(min_index + lookback, max_index, size=batch_size)
        else:
            if i + batch_size >= max_index:
                i = min_index + lookback

            # собираем  просто масив чисел по шагу
            rows = np.arange(i, min(i + batch_size, max_index))
            i += len(rows)

        # семплов  длина строк, колво в шаге, и кол-во признаков
        samples = np.zeros((len(rows), lookback // step, data.shape[-1]))
        targets = np.zeros(len(rows), )
        for j, row in enumerate(rows):
            # print(j, row)
            # от 0 до 1440 по 6
            indices = range(rows[j] - lookback, rows[j], step)
            samples[j] = data[indices]

            targets[j] = data[rows[j] + delay][1]
        yield samples, targets


def pysprkgenerate(df, lookback, delay, min_index, max_index, shuffle=False, batch_size=128, step=6):
    if max_index is None:
        max_index = df.count() - delay - 1
        i = min_index + lookback
    while 1:
        if shuffle:
            # batch_size рандомных чисел в диапазоне от мин-й точки отсчета до максимума
            rows = np.random.randint(min_index + lookback, max_index, size=batch_size)
        else:
            if i + batch_size >= max_index:
                i = min_index + lookback

            # собираем  просто масив чисел по шагу
            rows = np.arange(i, min(i + batch_size, max_index))
            i += len(rows)
        samples = np.zeros((len(rows), lookback // step, len(df.columns())))
        targets = np.zeros(len(rows), )
        for j, row in enumerate(rows):
            print(j, row)
            # от 0 до 1440 по 6
            samples[j] = df.select("*").offset(rows[j] - lookback).limit(lookback)

            targets[j] = df.select('T (degC)').offset(rows[j] + delay).limit(1)
        yield samples, targets
