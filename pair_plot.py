import matplotlib.pyplot as plt
from dataset import Dataset
from utils import parse_file_name, float_try_parse, get_color


def pair_plot(dataset, mask, sizex, sizey):
    first_feature = dataset.features[0]
    _, ax = plt.subplots(sizex, sizey)
    ax_index = 0
    for i in range(len(first_feature)):
        if i in mask and float_try_parse(first_feature[i]):
            for j in range(len(first_feature)):
                if j in mask and float_try_parse(first_feature[j]):
                    yval = []
                    xval = []
                    colors = []
                    for f in dataset.features:
                        if float_try_parse(f[i]) and float_try_parse(f[j]):
                            yval.append(float(f[i]))
                            xval.append(float(f[j]))
                            colors.append(get_color(f[0]))
                    ax_tindex = (ax_index // sizex, ax_index % sizey)
                    ax[ax_tindex].scatter(xval, yval, color=colors)
                    ax_index += 1
    plt.show()


if __name__ == '__main__':
    file_name = parse_file_name()
    dataset = Dataset(file_name)
    pair_plot(dataset, [i for i in range(len(dataset.features[0]))], 13, 13)
    pair_plot(dataset, [6, 7, 8, 11], 4, 4)
