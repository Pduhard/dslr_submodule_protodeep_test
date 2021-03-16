import matplotlib.pyplot as plt
from math import sqrt
from dataset import Dataset
from utils import parse_file_name, float_try_parse


def get_features_list(dataset):
    """ kind of removing non numeric features and transposing """
    features_list = []
    first_feature = dataset.features[0]
    for i in range(len(first_feature)):
        if float_try_parse(first_feature[i]) is True:
            # if i in [6, 7, 8, 11]:
            fl = []
            for f in dataset.features:
                if float_try_parse(f[i]) is True:
                    fl.append(float(f[i]))
            fl.sort()
            features_list.append(fl)
    return (features_list)


def compute_variance(fl, mean, count):
    variance = 0
    for v in fl:
        variance += (v - mean) ** 2
    return variance / count


def get_feature_stat(fl):
    fsum = sum(fl)
    fcount = len(fl)
    fmean = fsum / fcount
    fvar = compute_variance(fl, fmean, fcount)
    return {
        'Count': fcount,
        'Mean': fmean,
        'Std': sqrt(fvar),
        'Min': fl[0],
        '25%': fl[fcount // 4],
        'Med': fl[fcount // 2],
        '75%': fl[(fcount // 4) * 3],
        'Max': fl[-1]
    }


def describe(dataset):
    features_list = get_features_list(dataset)
    features_stat = [get_feature_stat(fl) for fl in features_list]
    hdr = '\t'
    for i in range(len(features_list)):
        hdr += dataset.features_name[i + 5][:13].ljust(14, ' ')
            # hdr += ('Feature ' + str(i)).ljust(14, ' ')
    print(hdr)
    for k in features_stat[0]:
        print(k, end='\t')
        for i in range(len(features_list)):
            print(str(round(features_stat[i][k], 6)).ljust(13, ' '), end=' ')
        print('')
    for index, f in enumerate(features_list):
        s = features_stat[index]
        plt.scatter([i for i in range(len(f))], f)
        plt.plot([0, len(f)], [s['Mean'], s['Mean']], color='green')
        plt.plot([0, len(f)], [s['Mean'], s['Mean']], color='green')
        plt.scatter([0], [s['Min']], s=100, color='red')
        plt.scatter([len(f) - 1], [s['Max']], s=100, color='red')
        plt.scatter([len(f) // 4], [s['25%']], s=100, color='yellow')
        plt.scatter([len(f) // 2], [s['Med']], s=100, color='yellow')
        plt.scatter([(len(f) // 4) * 3], [s['75%']], s=100, color='yellow')
        plt.show()


if __name__ == '__main__':
    file_name = parse_file_name()
    dataset = Dataset(file_name)
    describe(dataset)
