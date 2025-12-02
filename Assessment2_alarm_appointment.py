import numpy as np
import pandas as pd

def simulate(A, B, C, faulty):
    D = False if 1 in faulty else (A and B)
    E = True if 2 in faulty else (not A)  # Fixed: was "1" and "a"
    F = (B and C) if 3 in faulty else (B or C)  # Fixed: was "b and c"
    G = (D and E) if 4 in faulty else (D or E)
    H = False if 5 in faulty else (D and F)
    Z = (G and H) if 6 in faulty else (G or H)  # Fixed: was "z"
    return Z  # Fixed: indentation

A, B, C = True, True, True  # Fixed: indentation

for i in range(7):
    faulty = set() if i == 0 else {i}  # Fixed: indentation
    Z = simulate(A, B, C, faulty)
    name = "No fault" if i == 0 else f"Gate {i} faulty"  # Fixed: string formatting
    match = "<-- MATCH" if Z == False else ""
    print(f"{name}: Z={Z} {match}")  # Fixed: indentation