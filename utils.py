
import sys


def parse_file_name():
    file_name = "dataset_train.csv"
    for i, arg in enumerate(sys.argv):
        if i > 0:
            file_name = str(arg)
    return file_name


def float_try_parse(value):
    try:
        _ = float(value)
        return True
    except ValueError:
        return False


def vfloat_try_parse(value):
    try:
        val = float(value)
        return val, True
    except ValueError:
        return None, False


def get_color(house):
    if house == 'Gryffindor':
        return 'yellow'
    elif house == 'Slytherin':
        return 'green'
    elif house == 'Ravenclaw':
        return 'blue'
    elif house == 'Hufflepuff':
        return 'orange'
    return 'grey'


# def scatter_house_color(ax, xval, yval, houseval, target_house, color):
#     hxval = [x for i, x in enumerate(xval) if houseval[i] == target_house]
#     hyval = [y for i, y in enumerate(yval) if houseval[i] == target_house]
#     ax.scatter(hxval, hyval, color=color, alpha=0.25)