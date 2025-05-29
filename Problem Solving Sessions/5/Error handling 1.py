# function that prints each item in a sequence
"""
def print_sequence(sequence):
    try:
        for item in sequence:
            print(item, end=' ')
        print()
    except TypeError:
        print("Error: The provided input is not a valid sequence (like a list, string, or tuple).")

# Call the function here
if __name__ == "__main__":
    print_sequence([1, 2, 3, 4])
    print_sequence("hello")
    print_sequence((5, 6, 7))
    print_sequence(12345)     # Will raise and catch TypeError
    print_sequence(True)      # Will raise and catch TypeError
"""

# user number guessing game
"""
import random
def number_guessing_game():
    try:
        number_to_guess = random.randint(1, 10)
        attempts = 0
        max_attempts = 3
        print("Welcome to the Number Guessing Game!")
        print("I have selected a number between 1 and 10. Try to guess it!")

        while True:
            if attempts >= max_attempts:
                print("Sorry, you've exceeded the maximum number of attempts.")
                break

            guess = input("Enter your guess (or 'exit' to quit): ")
            if guess.lower() == 'exit':
                print("Thanks for playing!")
                break
            
            try:
                guess = int(guess)
                attempts += 1

                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    number_guessing_game()
"""

# file existence and reading checker
"""
def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while trying to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    filename = input("Enter the filename to open: ")
    open_file(filename)
"""