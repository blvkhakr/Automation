import json

# Function to extract information from a JSON file
def extract_information(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Iterate through the list of objects and extract information
    extracted_data = []
    for item in data:
        if 'KEY1' in item:
          value1 = item['KEY1']
          extracted_data.append(f"Key1: {'KEY1'}")

        if 'KEY2' in item:
          value2 = item['KEY2']
          extracted_data.append(f"Key2: {'KEY2'}")

      #add more logical if statements if needed

    return extracted_data

# Path to the JSON file
json_file = 'JSON_FILE_NAME.json'  # Replace with the path to your JSON file

# Call the function to extract information
extracted_data = extract_information(json_file)

# Print the extracted data
print("Extracted Data:")
for item in extracted_data:
    print(item)
