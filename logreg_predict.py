# import matplotlib.pyplot as plt
from dataset import Dataset
from Protodeep.model.model import Model
from Protodeep.layers.Dense import Dense
# from Protodeep.optimizers.SGD import SGD
from Protodeep.callbacks.EarlyStopping import EarlyStopping
from utils import parse_file_name
from scalers.StandardScaler import StandardScaler
from Preprocessing.Split import Split
import numpy as np

# def plot_history(history):
#     plt.plot(history['accuracy'])
#     plt.plot(history['val_accuracy'])
#     plt.ylabel('accuracy')
#     plt.xlabel('epoch')
#     plt.legend(['train', 'validation'], loc='upper left')
#     plt.show()

#     plt.plot(history['loss'])
#     plt.plot(history['val_loss'])
#     plt.ylabel('loss')
#     plt.xlabel('epoch')
#     plt.legend(['train', 'validation'], loc='upper left')
#     plt.show()


def get_house_name(prediction):
    label = np.argmax(prediction)
    if label == 0:
        return 'Gryffindor'
    elif label == 1:
        return 'Slytherin'
    elif label == 2:
        return 'Ravenclaw'
    elif label == 3:
        return 'Hufflepuff'
    return ''


if __name__ == "__main__":
    file_name = parse_file_name()
    dataset = Dataset(file_name)

    scaler = StandardScaler()
    scaler.load()
    dataset.train_features = scaler.transform(dataset.train_features)

    model = Model()
    model.add(Dense(units=4, activation='sigmoid'))
    model.compile(features_shape=4, metrics=['accuracy'],
                  optimizer='RMSProp')
    model.load_weights()
    with open('house.csv', 'w+') as outfile:
        outfile.write('Index,Hogwarts House\n')
        for i, feature in enumerate(dataset.train_features):
            o = str(i) + ',' + get_house_name(model.predict(feature)) + '\n'
            outfile.write(o)
