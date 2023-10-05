# The code reads an input CSV file with department information, maps each department to its corresponding department head, 
# and adds this information to a new column called 'Reports To.' Finally, it saves the result in a new CSV file.


import pandas as pd
import directory

def add_reports_to_column(input_csv):
    # Get the department directory
    department_directory = directory.create_department_lists()

    # Reverse the key-value pairs in department_directory to create a department_mapping dictionary
    department_mapping = {department: department_head for department_head, departments in department_directory.items() for department in departments}

    # Name of the department column
    department_column = 'Department'

    # Read the input CSV file into a DataFrame, in this case the headers start on row 7
    df = pd.read_csv(input_csv, header=6)

    # Insert column 'Reports To' to the DataFrame
    df.insert(3, 'Reports To', "")

    # Iterate through the DataFrame rows
    for index, row in df.iterrows():
        # Get the department name from the 'Department' column
        value_from_department = row[department_column]

        # Look up the department head in the department_mapping dictionary
        department_head = department_mapping.get(value_from_department, "Unknown")

        # Assign the department head to the "Reports To" column in the DataFrame
        df.at[index, 'Reports To'] = department_head

    # Save the processed DataFrame to a new CSV file called "output.csv"
    df.to_csv('output.csv', index=False)

