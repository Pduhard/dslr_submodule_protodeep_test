import numpy as np


class Split:

    @staticmethod
    def train_test_split(x, y, test_size=0.2, train_size=None,
                         seed=None, shuffle=True):
        x = np.array(x)
        y = np.array(y)
        if shuffle:
            if seed is not None:
                np.random.seed(seed)
            else:
                rng_state = np.random.get_state()
            np.random.shuffle(x)
            if seed is not None:
                np.random.seed(seed)
            else:
                np.random.set_state(rng_state)
            np.random.shuffle(y)
        split = int((1 - test_size) * len(x))
        return ((x[:split], y[:split]), (x[split:], y[split:]))