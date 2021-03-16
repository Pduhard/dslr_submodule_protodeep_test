from math import sqrt
import numpy as np
from utils import vfloat_try_parse


def translate_house(house):
    if house == 'Gryffindor':
        return [1, 0, 0, 0]
    elif house == 'Slytherin':
        return [0, 1, 0, 0]
    elif house == 'Ravenclaw':
        return [0, 0, 1, 0]
    elif house == 'Hufflepuff':
        return [0, 0, 0, 1]
    else:
        return None
    return []


class Dataset:

    def __init__(self, file_name, test_split=0.0):
        self.name = file_name.split('.')[0]
        self.features = self.parse_features(file_name)
        self.features_name = self.features.pop(0)
        self.select_features()
        # self.standardize_model_features()
        # if test_split > 0:
        #     self.split_dataset(test_split)
        # else:
        #     self.test_targets = None
        #     self.test_features = None

    def split_dataset(self, test_split):
        rng_state = np.random.get_state()
        np.random.shuffle(self.train_features)
        np.random.set_state(rng_state)
        np.random.shuffle(self.train_targets)
        split = int((1 - test_split) * len(self.train_features))
        self.test_features = self.train_features[split:]
        self.test_targets = self.train_targets[split:]
        self.train_features = self.train_features[:split]
        self.train_targets = self.train_targets[:split]

    def __str__(self):
        return '[{}]: size: {}'.format(self.name, len(self.features))

    def parse_features(self, file_name):
        fd = open(file_name, 'r')
        lines = fd.read().split('\n')
        return [x.split(',')[1:] for x in lines if len(x) > 0]

    # def standardize_model_features(self):
    #     for mf in self.train_features:
    #         for fi, f in enumerate(mf):
    #             fstat = self.features_stats[fi]
    #             mf[fi] = (f - fstat['Mean']) / fstat['Std']

    def select_features(self):
        features = []
        targets = []
        target_index = 0
        selected_features = [6, 7, 8, 11]
        features_mean = [[0, 0] for i in range(len(self.features[0]))]
        for feature in self.features:
            feat = []
            for i, f in enumerate(feature):
                if i in selected_features:
                    fval, success = vfloat_try_parse(f)
                    if success:
                        features_mean[i][0] += fval
                        features_mean[i][1] += 1
                    feat.append(fval)
                elif i == target_index:
                    targets.append(translate_house(f))
            features.append(feat)

        self.features_stats = [
            {
                'Mean': (f[0] / f[1]),
                'Std': 0,
                'Initial_count': f[1]
            } for f in features_mean if f != [0, 0]
        ]
        v = [0] * len(self.features_stats)
        for mf in features:
            for i, f in enumerate(mf):
                if f is None:
                    mf[i] = self.features_stats[i]['Mean']
                else:
                    v[i] += (f - self.features_stats[i]['Mean']) ** 2
        for i, s in enumerate(self.features_stats):
            s['Std'] = sqrt(v[i] / len(self.features))
        print(*self.features_stats, sep='\n')
        self.train_features = np.array(features).astype(float)
        self.train_targets = np.array(targets).astype(float)
