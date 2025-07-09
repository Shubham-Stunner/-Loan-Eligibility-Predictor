# model/generate_dummy_model.py

import sys
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Allow overriding the number of input features via CLI for flexibility.
num_features = int(sys.argv[1]) if len(sys.argv) > 1 else 7

# Generate dummy input and output matching the API's expected features
X = np.random.rand(100, num_features)
y = np.random.randint(0, 2, size=(100, 1))  # Binary output: approved (1) or not (0)

# Define a simple model with the correct input shape
model = Sequential([
    Dense(16, activation='relu', input_shape=(num_features,)),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile and train the model briefly
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=3, verbose=1)

# Save the model
model.save("model/loan_model_v1.h5")

print("✅ Dummy model saved as model/loan_model_v1.h5")
