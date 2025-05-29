"""
This code initializes an array with five None values and prints each value in the array.
array = [None, None, None, None, None]

for i in array:
    print(i)
"""

"""
count = 0
array = []

for count in range(1, 1000001):
    array.append(count)
print(array)
"""

"""
# Function that takes a string parameter and separates each character into an item in an array
def string_to_array(string):
    array = []
    # Loop through each character in the string
    for char in string:
        array.append(char)  # Add the character to the array
    return array  # Return the resulting array

if __name__ == "__main__":
    string = "Hello, World!"  # Example string
    result = string_to_array(string)  # Convert string to array of characters
    print(result)  # Print the resulting array
"""

"""
# array failure testing (TDD) - characterization test - tests done after the code is written
def test_invalid_index_access():
    test_array = [10, 20, 30]
    index_to_test = 5
    try:
        test_array[index_to_test]
        print("FAIL: Invalid index did not raise IndexError.")
    except IndexError:
        print("PASS: Invalid index correctly raised IndexError.")
"""

"""
# linear search implementation with slicing implementation
import time
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for item in arr:
        if item == target:
            return True
    return False

def benchmark_linear_search():
    sizes = [0, 200_000, 400_000, 600_000, 800_000, 1_000_000]
    times = []

    # Create one large array
    big_array = list(range(1_000_000))

    for size in sizes:
        test_array = big_array[:size]
        target = -1  # Use a value NOT in the array to force worst-case scenario

        start = time.perf_counter()
        linear_search(test_array, target)
        end = time.perf_counter()

        elapsed = end - start
        times.append(elapsed)
        print(f"Size: {size}, Time: {elapsed:.6f} sec")

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, times, marker='o')
    plt.title("Linear Search Time vs Array Size")
    plt.xlabel("Array Size")
    plt.ylabel("Search Time (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Run it
benchmark_linear_search()

"""