# example1_simple_usage.py

# Import necessary modules or functions from your project
from biomechanical_simulation import simulate_limb

# Define input parameters
limb_length = 0.5  # meters
muscle_force = 100  # Newtons

# Call the simulate_limb function with input parameters
result = simulate_limb(limb_length, muscle_force)

# Display simulation results
print("Simulation Results:")
print(result)
