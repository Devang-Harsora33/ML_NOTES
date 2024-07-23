import pandas as pd
import os

current_dir = os.path.dirname(__file__)

file_path = os.path.join(current_dir, 'data.csv')

# Check if the file exists
if os.path.exists(file_path):
    try:
        df = pd.read_csv(file_path)
        print(df.corr())#Note: The corr() method ignores "not numeric" columns.
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
else:
    print(f"The file {file_path} does not exist.")
