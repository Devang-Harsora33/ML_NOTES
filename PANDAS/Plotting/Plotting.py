import pandas as pd
import os
import matplotlib.pyplot as plt

current_dir = os.path.dirname(__file__)

file_path = os.path.join(current_dir, 'data.csv')

# Check if the file exists
if os.path.exists(file_path):
    try:
        df = pd.read_csv(file_path)
        df.plot()
        plt.show()
        df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

        plt.show()    
        df["Duration"].plot(kind = 'hist')

        plt.show()  
    except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
    else:
        print(f"The file {file_path} does not exist.")
