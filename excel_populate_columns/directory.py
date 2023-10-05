# The script reads data from a spreadsheet (either in CSV format)
# that contains information about department heads and their associated departments.
# It then organizes this data into unique lists for each department head. The script
# iterates through the rows of the spreadsheet, identifying the department head and
# the department associated with each row, and adds the department to the respective
# department head's list. Finally, it prints out these unique lists, showing the
# departments assigned to each department head.
import pandas as pd

def create_department_lists():
    # Read the CSV file into a DataFrame, assuming the first row is the header
    df = pd.read_csv("FILENAME")

    # Initialize a dictionary to store the department lists for each department head
    department_directory = {}

    # Iterate through the rows of the DataFrame
    for index, row in df.iterrows():
        department_head = row['Director']
        department = row['Department']

        # Check if the department head already exists in department_directory
        if department_head in department_directory:
            # If it exists, then append the department to the director
            department_directory[department_head].append(department)
        else:
            # If it doesn't exist, create a new key with the value
            department_directory[department_head] = [department]

    # Return a dictionary that contains department heads (as keys) and their associated department lists (as values)
    return department_directory


