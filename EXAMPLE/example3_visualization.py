# example3_visualization.py

# Import necessary modules or functions from your project
import matplotlib.pyplot as plt
from biomechanical_simulation import simulate_limb

# Define input parameters
limb_length = 0.5  # meters
muscle_force = 100  # Newtons

# Call the simulate_limb function with input parameters
result = simulate_limb(limb_length, muscle_force)

# Visualize simulation results
plt.plot(result['time'], result['displacement'])
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('Limb Displacement over Time')
plt.grid(True)
plt.show()
