import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# SIR model differential equations
def sir_model(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# Parameters for COVID-19
beta = 0.3  # Transmission rate
gamma = 0.1  # Recovery rate

# Initial conditions: S, I, R
initial_conditions = [0.99, 0.01, 0.0]

# Time points
t = np.linspace(0, 200, 200)

# Solve the SIR differential equations
solution = odeint(sir_model, initial_conditions, t, args=(beta, gamma))

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, solution[:, 0], label='Susceptible')
plt.plot(t, solution[:, 1], label='Infected')
plt.plot(t, solution[:, 2], label='Recovered')
plt.title("Basic SIR Model for COVID-19 Prediction")
plt.xlabel("Time")
plt.ylabel("Population Fraction")
plt.legend()
plt.grid(True)
plt.show()
