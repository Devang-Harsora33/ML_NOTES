import pandas as pd
import os

current_dir = os.path.dirname(__file__)

file_path = os.path.join(current_dir, 'data.csv')

# Check if the file exists
if os.path.exists(file_path):
    try:
        df = pd.read_csv(file_path)

        #Replacing Values
        #One way to fix wrong values is to replace them with something else.
        #In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:
        df.loc[7,'Duration'] = 45

        print(df.to_string())

        for x in df.index:
          if df.loc[x, "Duration"] > 120:
            df.loc[x, "Duration"] = 120

        print(df.to_string())

        #Removing Rows
        for x in df.index:
          if df.loc[x, "Duration"] > 120:
            df.drop(x, inplace = True)

        #remember to include the 'inplace = True' argument to make the changes in the original DataFrame object instead of returning a copy

        print(df.to_string())

    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
else:
    print(f"The file {file_path} does not exist.")


