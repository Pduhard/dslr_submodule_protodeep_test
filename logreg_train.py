import matplotlib.pyplot as plt
from dataset import Dataset
from Protodeep.model.model import Model
from Protodeep.layers.Dense import Dense
# from Protodeep.optimizers.SGD import SGD
from Protodeep.callbacks.EarlyStopping import EarlyStopping
from utils import parse_file_name
from scalers.StandardScaler import StandardScaler
# from scalers.NormalScaler import NormalScaler
from Preprocessing.Split import Split


def plot_history(history):
    plt.plot(history['accuracy'])
    plt.plot(history['val_accuracy'])
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()

    plt.plot(history['loss'])
    plt.plot(history['val_loss'])
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()


if __name__ == "__main__":
    file_name = parse_file_name()
    dataset = Dataset(file_name)

    scaler = StandardScaler().fit(dataset.train_features)
    dataset.train_features = scaler.transform(dataset.train_features)

    print(dataset.train_features.tolist())

    ((x_train, y_train), (x_test, y_test)) = Split.train_test_split(
        dataset.train_features, dataset.train_targets)
    model = Model()
    # model.add(Dense(units=16, activation='relu'))
    # model.add(Dense(units=16, activation='relu'))
    model.add(Dense(units=4, activation='sigmoid'))
    model.compile(features_shape=4, metrics=['accuracy'],
                  optimizer='RMSProp')
    history = model.fit(x_train, y_train, validation_data=(x_test, y_test),
                        callbacks=[EarlyStopping(patience=7)], epochs=200)
    scaler.save()
    model.save_weights()
    plot_history(history)
