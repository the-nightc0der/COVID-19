import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from sklearn.linear_model import LinearRegression

# Compartmental SEIR model parameters
beta = 0.3
sigma = 0.1
gamma = 0.05

# Machine learning model
ml_model = LinearRegression()

# Time points
t = np.linspace(0, 200, 200)

# Compartmental SEIR model differential equations
def seir_model(y, t, beta, sigma, gamma):
    S, E, I, R = y
    dSdt = -beta * I * S
    dEdt = beta * I * S - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]

# Initial conditions for SEIR model
initial_conditions_seir = [0.9, 0.1, 0.0, 0.0]

# Solve the SEIR model
solution_seir = odeint(seir_model, initial_conditions_seir, t, args=(beta, sigma, gamma))

# Use SEIR model output to train machine learning model
X = solution_seir[:, 2]  # Infected individuals
y = solution_seir[:, 3]  # Recovered individuals
ml_model.fit(X.reshape(-1, 1), y)

# Predict using the machine learning model
y_pred = ml_model.predict(X.reshape(-1, 1))

# Plot the SEIR model output and machine learning predictions
plt.plot(t, solution_seir[:, 2], label='Infected (SEIR)')
plt.plot(t, y_pred, label='Recovered (ML)')
plt.title("Hybrid Model for COVID-19 Prediction")
plt.xlabel("Time")
plt.ylabel("Individuals")
plt.legend()
plt.grid(True)
plt.show()
