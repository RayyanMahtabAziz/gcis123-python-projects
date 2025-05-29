"""
# increments each item in the array by a number input by the user
# unoptimized version
adder = int(input("Enter a number: "))
array = [1, 2, 3, 4, 5]
def add_to_number(array):
    for i in array:
        print(i + adder)   

if __name__ == "__main__":
    add_to_number(array)  # Call the function to add the number to each element in the array
    print("Done adding to array elements.") 

# optimized version:
def add_to_array(array, number):
# below we used a list comprehension for our iteration
    return [i + number for i in array]

if __name__ == "__main__":
    try:
        adder = int(input("Enter a number: "))
        array = [1, 2, 3, 4, 5]
        result = add_to_array(array, adder)
        
        for value in result:
            print(value)
        
        print("Done adding to array elements.")
    except ValueError:
        print("Please enter a valid integer.")

# solved using recursion
def add_amount_recursive(an_array, amount, index=0):
    # Base case: if index reaches the end of the array, stop recursion
    if index == len(an_array):
        return

    # Add the amount to the current element
    an_array[index] += amount

    # Recursive call to the next index
    add_amount_recursive(an_array, amount, index + 1)
"""


