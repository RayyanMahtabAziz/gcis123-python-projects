import matplotlib.pyplot as plt
# Function to get lab average and plot grades for a specific student

def get_lab_average_and_plot(filename, first_name, last_name):
    try:
        with open(filename, 'r') as inputfile:
            for line in inputfile:
                parts = line.strip().split(',')
                if len(parts) < 10:
                    continue
                
                if parts[0].strip() == first_name and parts[1].strip() == last_name:
                    try:
                        grades = [float(parts[i]) for i in range(2, 10)]  # columns 2–9
                        average = sum(grades) / len(grades)

                        # Plotting the grades
                        plt.figure(figsize=(8, 5))
                        plt.plot(range(1, 9), grades, marker='o', linestyle='-', color='blue')
                        plt.title(f"Lab Grades for {first_name} {last_name}")
                        plt.xlabel("Lab Number")
                        plt.ylabel("Grade")
                        plt.xticks(range(1, 9))
                        plt.grid(True)
                        plt.tight_layout()
                        plt.show()

                        return average
                    except ValueError:
                        print(f"Error converting grades to float for {first_name} {last_name}.")
                        return None
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return None


# Example test call
"""
if __name__ == "__main__":
    avg = get_lab_average_and_plot("grades.csv", "John", "Doe")
    if avg is not None:
        print(f"Lab average for John Doe: {avg:.2f}")
    else:
        print("Student not found or an error occurred.")
"""
# Uncomment the example test call to run the function with a specific file and student name.
