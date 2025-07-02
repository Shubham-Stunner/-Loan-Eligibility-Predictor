import numpy as np
import tensorflow as tf


def generate_data(samples=1000):
    X = np.random.rand(samples, 7)
    y = (X.sum(axis=1) > 3.5).astype(int)
    return X, y


def train():
    X, y = generate_data()
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(16, activation='relu', input_shape=(7,)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, y, epochs=5)
    model.save('model/loan_model_v1.h5')


if __name__ == '__main__':
    train()
