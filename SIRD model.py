import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# SIRD model differential equations
def sird_model(y, t, beta, gamma, delta):
    S, I, R, D = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I - delta * I
    dRdt = gamma * I
    dDdt = delta * I
    return [dSdt, dIdt, dRdt, dDdt]

# Parameters for COVID-19
beta = 0.3   # Transmission rate
gamma = 0.1  # Recovery rate
delta = 0.01 # Death rate

# Initial conditions: S, I, R, D
initial_conditions = [0.99, 0.01, 0.0, 0.0]

# Time points
t = np.linspace(0, 200, 200)

# Solve the SIRD differential equations
solution = odeint(sird_model, initial_conditions, t, args=(beta, gamma, delta))

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, solution[:, 0], label='Susceptible')
plt.plot(t, solution[:, 1], label='Infected')
plt.plot(t, solution[:, 2], label='Recovered')
plt.plot(t, solution[:, 3], label='Deaths')
plt.title("Basic SIRD Model for COVID-19 Prediction")
plt.xlabel("Time")
plt.ylabel("Population Fraction")
plt.legend()
plt.grid(True)
plt.show()
