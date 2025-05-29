import csv
"""
# Function to calculate the average grade for a specific section in a CSV file
# and print the result.
def section_avg(filename, section_number, grade_index):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)

            header = next(reader)  # Skip header if present
            total = 0
            count = 0

            for row in reader:
                try:
                    if int(row[1]) == section_number:  # Assuming section is in column 1
                        grade = float(row[grade_index])
                        total += grade
                        count += 1
                except (ValueError, IndexError):
                    continue  # Skip rows with invalid data

            if count > 0:
                average = total / count
                print(f"Section Average: {average:.2f}")
            else:
                print(f"No data found for section {section_number}.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    filename = input("Enter the filename: ")
    section_number = int(input("Enter the section number: "))
    grade_index = int(input("Enter the grade index (0-based): "))
    section_avg(filename, section_number, grade_index)  
"""

"""
# Function to read a CSV file and print the name and address of each entry.
def name_and_address(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                print(row[0], row[1])
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
"""