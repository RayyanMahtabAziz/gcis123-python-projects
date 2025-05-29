# Author: Rayyan Mahtab

# Code 1
# simple hashing function using ASCII values summations.
def simple_ascii_hash(s):
    return sum(ord(char) for char in s)


"""
Speed - Simple Code thus it's very fast.
Consistency - Deterministic - same input always yields same output.
Collision Frequency - Quite frequent as " abc" and "cab" will yield the same hash.
"""

#Code 2
#using a polynomial rolling hash function (2 different formulas)
"""
def polynomial_rolling_hash(s, base=31, mod=10**9 + 9):
    hash_value = 0
    # below we use enumerate as we need the index of each character for the polynomial calculation.
    for i, char in enumerate(s):
        hash_value = (hash_value + (ord(char) - ord('a') + 1) * pow(base, i, mod)) % mod
    return hash_value

def polynomial_hash_optimized(s):
hash_value = 0
power = 1  # 31^0
for c in reversed(s):
    hash_value += ord(c) * power
    power *= 31
return hash_value

# since its a rolling hash, it can be used to compute the hash of a substring in O(1) time after O(n) preprocessing.
# Speed - Fast, O(n) for preprocessing and O(1) for substring hash retrieval.
# Consistency - Deterministic, same input always yields same output.
# Collision Frequency - Less frequent than simple ASCII hash, but still possible.

"""

# Code 3
# Caesar Cipher Implementation
"""
KEY = 3
ALPHABET_SIZE = 26

def encrypt(text):
    # Encrypts a string using Caesar cipher.
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + KEY) % ALPHABET_SIZE + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + KEY) % ALPHABET_SIZE + ord('a'))
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

def decrypt(text):
    # Decrypts a string using Caesar cipher.
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') - KEY) % ALPHABET_SIZE + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') - KEY) % ALPHABET_SIZE + ord('a'))
        else:
            result += char
    return result

def handle_choice():
    # Handles the user choice for encryption or decryption.
    while True:
        choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").strip().lower()
        if choice == "encrypt":
            text = input("Enter the text to encrypt: ").strip()
            encrypted = encrypt(text)
            print("Encrypted text:", encrypted, "\n")
            break
        elif choice == "decrypt":
            text = input("Enter the text to decrypt: ").strip()
            decrypted = decrypt(text)
            print("Decrypted text:", decrypted, "\n")
            break
        else:
            print("Invalid input. Please type 'encrypt' or 'decrypt'.")

def repeat_menu():
    # Asks the user if they want to repeat the process.
    while True:
        again = input("Do you want to encrypt/decrypt another text? (yes/no): ").strip().lower()
        if again in ["yes", "y"]:
            return True
        elif again in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def main():
    print("=== Caesar Cipher Program ===")
    while True:
        handle_choice()
        if not repeat_menu():
            break
    print("\nThank you for using the Caesar Cipher program!")

if __name__ == "__main__":
    main()
"""