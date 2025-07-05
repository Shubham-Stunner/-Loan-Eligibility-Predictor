# model/generate_dummy_model.py

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Generate dummy input and output
X = np.random.rand(100, 3)  # 3 features: age, income, credit score
y = np.random.randint(0, 2, size=(100, 1))  # Binary output: approved (1) or not (0)

# Define a simple model
model = Sequential([
    Dense(8, activation='relu', input_shape=(3,)),
    Dense(4, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile and train the model briefly
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=3, verbose=1)

# Save the model
model.save("model/loan_model_v1.h5")

print("✅ Dummy model saved as model/loan_model_v1.h5")
