import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define number of samples and features
num_samples = 5000
num_features = 7

# Data containers
X = []
y = []

# Generate synthetic rule-based training data
for _ in range(num_samples):
    age = np.random.randint(18, 70)
    income = np.random.randint(10000, 1000000)
    credit_score = np.random.randint(300, 850)
    loan_amount = np.random.randint(5000, 500000)
    loan_term = np.random.choice([5, 10, 15, 20, 30])
    emp_years = np.random.randint(0, 40)
    debt = np.random.randint(0, 200000)

    features = [age, income, credit_score, loan_amount, loan_term, emp_years, debt]
    X.append(features)

    # Rule-based loan approval logic
    approved = (
        income > 25000 and
        credit_score >= 650 and
        loan_amount < income * 10 and
        emp_years >= 1 and
        debt < loan_amount * 0.5
    )

    y.append([int(approved)])

# Convert to numpy arrays
X = np.array(X, dtype=np.float32)
y = np.array(y, dtype=np.float32)

# Define model
model = Sequential([
    Dense(32, activation='relu', input_shape=(num_features,)),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X, y, epochs=10, batch_size=32, verbose=1)

# Save model
model.save("model/loan_model_v1.h5")

print("✅ Rule-based trained model saved as model/loan_model_v1.h5")
