import sys
import matplotlib.pyplot as plt
from dataset import Dataset
from utils import parse_file_name, float_try_parse


def subplot_histogram(ax, house_val, xrng, color):
    ax.hist(house_val, range=xrng, color=color, edgecolor='black')


def plot_histogram(fl, xrng, feature_name):
    _, ax = plt.subplots(2, 2)
    subplot_histogram(ax[0, 0], fl['Gryffindor'], xrng, 'yellow')
    subplot_histogram(ax[0, 1], fl['Hufflepuff'], xrng, 'orange')
    subplot_histogram(ax[1, 0], fl['Ravenclaw'], xrng, 'blue')
    subplot_histogram(ax[1, 1], fl['Slytherin'], xrng, 'green')
    plt.suptitle('School Subject: {}'.format(feature_name))
    plt.show()


def get_xrng(features, i):
    xrmin = sys.float_info.max
    xrmax = -1 * sys.float_info.max
    fsum = 0
    fcount = 0
    for f in features:
        feature = f[i]
        if float_try_parse(feature) is True:
            fcount += 1
            fsum += float(feature)
            fl[f[0]].append(float(feature))
            if (xrmin > float(feature)):
                xrmin = float(feature)
            if (xrmax < float(feature)):
                xrmax = float(feature)
    return [xrmin, xrmax]


if __name__ == '__main__':
    file_name = parse_file_name()
    dataset = Dataset(file_name)
    first_feature = dataset.features[0]
    for i in range(len(first_feature)):
        if float_try_parse(first_feature[i]) is True:
            fl = {
                'Gryffindor': [],
                'Ravenclaw': [],
                'Slytherin': [],
                'Hufflepuff': []
            }
            xrng = get_xrng(dataset.features, i)
            plot_histogram(fl, xrng, dataset.features_name[i])
