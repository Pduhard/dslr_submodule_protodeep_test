import sys
import matplotlib.pyplot as plt
from math import sqrt, exp
from random import random
from old_dataset import Dataset
import numpy as np


def parse_file_name():
    file_name = "dataset_train.csv"
    for i, arg in enumerate(sys.argv):
        if i > 0:
            file_name = str(arg)
    return file_name

def floatTryParse(value):
    try:
        _ = float(value)
        return True
    except ValueError:
        return False

def scatter_house_color(ax, xval, yval, houseval, target_house, color):
    hxval = [x for i, x in enumerate(xval) if houseval[i] == target_house]
    hyval = [y for i, y in enumerate(yval) if houseval[i] == target_house]
    ax.scatter(hxval, hyval, color=color, alpha=0.25)

def initialize_network_param():
    return [[0 for i in range(dataset.model_features_count)] for j in range(4)], [0, 0, 0, 0]


def activation(z):
    # sigmoid
    return 1 / (1 + exp(-z))

def sigmoid_derivative(z):
    return activation(z) * (1 - activation(z))

def pre_activation(weights, bias, features):
    z = 0
    for i in range(len(features)):
        z += weights[i] * features[i]
    z += bias
    return z

def compute_error(y, i, target):
    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
    # print(f"find: {houses[i]}{y} target  {target}")
    if target == houses[i]:
        return y - 1
    else:
        return y
    
    
    # care !!
    # prediction = 

def train(dataset):
    weights, bias = initialize_network_param()
    batch_size = 1
    epoch = 10000
    learning_rate = 0.001
    print (weights)
    print (bias)
    for e in range(epoch + 1):
        accuracy = 0
        wgradients = [0] * 16
        bgradients = [0] * 4
        if not e % (epoch / 10):
            print(f"epoch: {e}/{epoch}")
        batch = []
        for i in range(batch_size):
            batch.append(dataset.model_features[int(random() * len(dataset.model_features))])
        # s = 0
        for f in batch:
            # best = -1
            # maxy = 0
            for i in range(4): # 4 outputs
                z = pre_activation(weights[i], bias[i], f["features"])
                y = activation(z)
                # if y > maxy:
                #     best = i
                #     maxy = y
                
                # print (y)
                error = compute_error(y, i, f["target"]) # y - t with gryfindor etc
                for j in range(4):
                    wgradients[(i * 4) + j] += error * sigmoid_derivative(z) * f["features"][j]
                bgradients[i] += error * sigmoid_derivative(z)
                # print (z, y)
            # if ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"][best] == f["target"]:
            #     s += 1
            # scsc = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"][best]
            # print(f"{scsc}{f['")
        for i in range(16):
            weights[i//4][i%4] -= learning_rate * wgradients[i]
        for i in range(4):
            bias[i] -= learning_rate * bgradients[i]
        # weights -= 
    print("")
        # prediction
    return weights, bias

if __name__ == "__main__":
    file_name = parse_file_name()
    dataset = Dataset(file_name)
    weights, bias = train(dataset)

    print (weights, bias)
    s = 0
    for f in dataset.model_features:
        best = -1
        maxy = 0
        for i in range(4): # 4 outputs
            z = pre_activation(weights[i], bias[i], f["features"])
            y = activation(z)
            if y > maxy:
                best = i
                maxy = y
        if ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"][best] == f["target"]:
            s += 1
    print(f"accuracy: {round(s/len(dataset.model_features) * 100, 4)}%: {s}/{len(dataset.model_features)}")
# (y - t)(a(x)(1 - a(x)))
# (y - t)(ax - ax²)
# ax * y + ax² * y - ax * t + ax² * t

