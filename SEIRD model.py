import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# SEIRD model differential equations
def seird_model(y, t, beta, gamma, sigma, delta):
    S, E, I, R, D = y
    dSdt = -beta * S * I
    dEdt = beta * S * I - sigma * E
    dIdt = sigma * E - (gamma + delta) * I
    dRdt = gamma * I
    dDdt = delta * I
    return [dSdt, dEdt, dIdt, dRdt, dDdt]

# Parameters for COVID-19
beta = 0.3   # Transmission rate
gamma = 0.1  # Recovery rate
sigma = 0.2  # Exposed to Infected rate
delta = 0.01 # Death rate

# Initial conditions: S, E, I, R, D
initial_conditions = [0.99, 0.01, 0.0, 0.0, 0.0]

# Time points
t = np.linspace(0, 200, 200)

# Solve the SEIRD differential equations
solution = odeint(seird_model, initial_conditions, t, args=(beta, gamma, sigma, delta))

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, solution[:, 0], label='Susceptible')
plt.plot(t, solution[:, 1], label='Exposed')
plt.plot(t, solution[:, 2], label='Infected')
plt.plot(t, solution[:, 3], label='Recovered')
plt.plot(t, solution[:, 4], label='Deaths')
plt.title("Basic SEIRD Model for COVID-19 Prediction")
plt.xlabel("Time")
plt.ylabel("Population Fraction")
plt.legend()
plt.grid(True)
plt.show()
