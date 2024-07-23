import pandas as pd
import os

# Get the current working directory
current_dir = os.path.dirname(__file__)

# Define the file path relative to the current directory
file_path = os.path.join(current_dir, 'data.csv')

# Check if the file exists
if os.path.exists(file_path):
    try:
        df = pd.read_csv(file_path)

        print(df.to_string()) 
        print(df) 
        print(pd.options.display.max_rows) 
        pd.options.display.max_rows = 99

        df = pd.read_csv(file_path)
        print(df) 

    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
else:
    print(f"The file {file_path} does not exist.")
