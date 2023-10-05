import os
import mapping



if __name__ == "__main__":

    input_csv_file = input("Enter the file name: ")

    file_name = input_csv_file + ".csv"
    file_path = "FILE_PATH"
    file = os.path.join(file_path, file_name)

    mapping.add_reports_to_column(file)
