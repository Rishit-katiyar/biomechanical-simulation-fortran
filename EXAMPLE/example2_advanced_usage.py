# example2_advanced_usage.py

# Import necessary modules or functions from your project
from biomechanical_simulation import LimbSimulator, Muscle, Bone

# Create instances of Bone and Muscle objects
femur = Bone("Femur", length=0.3, diameter=0.05)
quadriceps = Muscle("Quadriceps", force=150)

# Create a LimbSimulator object and add bones and muscles to it
limb_simulator = LimbSimulator()
limb_simulator.add_bone(femur)
limb_simulator.add_muscle(quadriceps)

# Run the simulation
result = limb_simulator.run_simulation()

# Display simulation results
print("Advanced Simulation Results:")
print(result)
