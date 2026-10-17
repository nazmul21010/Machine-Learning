import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Dataset
# -----------------------------
X = np.array([1, 2, 3, 4, 5])
y = np.array([50, 55, 65, 70, 75])

# -----------------------------
# 2. Initialize parameters
# -----------------------------
m = 0
c = 0

learning_rate = 0.01
epochs = 1000

# -----------------------------
# 3. Cost Function
# -----------------------------
def cost_function(X, y, m, c):
    n = len(X)
    total_error = 0

    for i in range(n):
        y_pred = m * X[i] + c
        total_error += (y[i] - y_pred) ** 2

    return total_error / n

# -----------------------------
# 4. Gradient Descent
# -----------------------------
def gradient_descent(X, y, m, c, lr):
    n = len(X)
    dm = 0
    dc = 0

    for i in range(n):
        y_pred = m * X[i] + c
        error = y[i] - y_pred

        dm += -2 * X[i] * error
        dc += -2 * error

    m = m - lr * (dm / n)
    c = c - lr * (dc / n)

    return m, c

# -----------------------------
# 5. Training Loop
# -----------------------------
for i in range(epochs):
    m, c = gradient_descent(X, y, m, c, learning_rate)

    if i % 100 == 0:
        loss = cost_function(X, y, m, c)
        print(f"Epoch {i}, Loss: {loss:.4f}, m: {m:.4f}, c: {c:.4f}")

# -----------------------------
# 6. Prediction function
# -----------------------------
def predict(x):
    return m * x + c

print("\nFinal Model:")
print("m =", m)
print("c =", c)

print("\nPrediction for 6 hours study:", predict(6))

# -----------------------------
# 7. Visualization
# -----------------------------
plt.scatter(X, y, color='blue', label="Data Points")
plt.plot(X, m * X + c, color='red', label="Best Fit Line")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Linear Regression From Scratch")
plt.legend()
plt.show()