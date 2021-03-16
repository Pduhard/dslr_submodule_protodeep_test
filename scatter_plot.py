import matplotlib.pyplot as plt
from dataset import Dataset
from utils import parse_file_name, float_try_parse, get_color

if __name__ == "__main__":
    file_name = parse_file_name()
    dataset = Dataset(file_name)
    first_feature = dataset.features[0]
    for i in range(len(first_feature)):
        if float_try_parse(first_feature[i]):
            _, ax = plt.subplots(3, 4)
            ax_index = 0
            for j in range(len(first_feature)):
                if float_try_parse(first_feature[j]) and i != j:
                    yval = []
                    xval = []
                    colors = []
                    for f in dataset.features:
                        if float_try_parse(f[i]) and float_try_parse(f[j]):
                            yval.append(float(f[i]))
                            xval.append(float(f[j]))
                            colors.append(get_color(f[0]))
                    ax_tindex = (ax_index // 4, ax_index % 4)
                    ax[ax_tindex].set_title(dataset.features_name[j])
                    ax[ax_tindex].scatter(xval, yval, color=colors)
                    ax_index += 1
            plt.suptitle(f'{dataset.features_name[i]} according to :')
            plt.subplots_adjust(left=None, bottom=None, right=None,
                                top=None, wspace=None, hspace=0.3)
            plt.show()
