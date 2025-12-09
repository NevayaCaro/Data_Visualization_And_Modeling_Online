import os
import pandas as pd

# 1. Show where the notebook is currently running
print("Current Working Directory:")
print(os.getcwd())

print("\nFiles in this folder:")
print(os.listdir())

# 2. Try loading the file from multiple possible locations
possible_paths = [
    "titanic_passengers.csv",
    "./titanic_passengers.csv",
    "Lab/titanic_passengers.csv",
    "./Lab/titanic_passengers.csv",
    "Data_Visualization_And_Modeling_Online/Lab/titanic_passengers.csv",
    "./Data_Visualization_And_Modeling_Online/Lab/titanic_passengers.csv"
]

df = None

for path in possible_paths:
    try:
        df = pd.read_csv(path)
        print(f"\nSUCCESS: Loaded file from → {path}")
        break
    except FileNotFoundError:
        continue

# 3. If file not found
if df is None:
    print("\nERROR: Could not find titanic_passengers.csv in any common folder.")
    print("Upload the file OR show me your folder structure so I can give exact path.")
else:
    print("\nPreview of the Titanic DataFrame:")
    df.head()
