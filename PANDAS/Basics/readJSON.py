import pandas as pd
import os

# Get the current working directory
current_dir = os.path.dirname(__file__)

# Define the file path relative to the current directory
file_path = os.path.join(current_dir, 'data.json')

# Check if the file exists
if os.path.exists(file_path):
    try:
        df = pd.read_json(file_path)

        print(df.head(10))# normal head() ll return 5 rows
        print(df.tail()) 
        print(df.to_string()) 
        print(df) 
        print(pd.options.display.max_rows) 
        pd.options.display.max_rows = 99

        df = pd.read_json(file_path)
        print(df) 
        print(df.info()) 

    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
else:
    print(f"The file {file_path} does not exist.")


data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 