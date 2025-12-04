import numpy as np
import pandas as pd

def simulate(A, B, C, faulty):
    D = False if 1 in faulty else (A and B)
    E = True if 2 in faulty else (not A)  
    F = (B and C) if 3 in faulty else (B or C)  
    G = (D and E) if 4 in faulty else (D or E)
    H = False if 5 in faulty else (D and F)
    Z = (G and H) if 6 in faulty else (G or H) 
    return Z  

# Engineer inputs and observation
A, B, C = True, True, True
observed_Z = False

# Step 1: Find which gates cause the observed output
matching_faults = []

for i in range(1, 7):
    # Simulate the circuit assuming ONLY gate i is faulty
    faulty_set = {i}
    Z = simulate(A, B, C, faulty_set)
    
    # Check if this simulation matches the engineer's observation
    if Z == observed_Z:
        matching_faults.append(i)

# Step 2: Determine status based on matches
print(f"Observation: Input=(T,T,T) -> Output={observed_Z}")
print("-" * 30)

for i in range(1, 7):
    if i in matching_faults:
        # If this gate explains the error (and is the only one), it is the culprit
        if len(matching_faults) == 1:
            print(f"Gate {i}: Must be Faulty")
        else:
            # If multiple gates could explain it, we would be uncertain
            print(f"Gate {i}: Uncertain")
    else:
        # If this gate being faulty would produce the WRONG output, it must be normal
        print(f"Gate {i}: Must be Normal")