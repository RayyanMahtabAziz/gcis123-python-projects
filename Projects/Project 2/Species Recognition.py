# GCIS-123 – Assignment 2 (Parts A–F)
# Author: Rayyan Mahtab
# Date: 28/05/2021
# This program helps scientists identify DNA patterns for different species,
# compare DNA similarities, and add new species to the database.

import os

# === Species Dictionary (initial data) ===
SpeciesDict = {
    "specieA": "DNA1.txt",
    "specieB": "DNA2.txt"
}

# A) Get file path for a species
def getFile(sName):
    """Return file name for a species, or 'Specie not found.' if not found."""
    return SpeciesDict.get(sName, "Specie not found.")

# B) Display DNA from file
def retDNA(DNAfile):
    """Print DNA content from a file path, handle exceptions."""
    try:
        with open(DNAfile, 'r') as file:
            dna = file.read().strip()
            print(f"DNA strand from '{DNAfile}':\n{dna}")
    except FileNotFoundError:
        print(f"Error: File '{DNAfile}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# C) Add species to the dictionary
def addSpecie(sName, fileName):
    """Add a new species and its DNA file to the dictionary."""
    if sName in SpeciesDict:
        print(f"Species '{sName}' already exists.")
    else:
        SpeciesDict[sName] = fileName
        print(f"Species '{sName}' added with file '{fileName}'.")

# D) Create DNA file for new species and register
def addDNA(specieName):
    """Accept DNA from user and save to file; register species."""
    # Find the next unused DNA file number
    used_files = [f for f in os.listdir() if f.startswith("DNA") and f.endswith(".txt")]
    numbers = [int(f[3:-4]) for f in used_files if f[3:-4].isdigit()]
    next_num = max(numbers, default=0) + 1
    new_file = f"DNA{next_num}.txt"

    # Read DNA from user
    dna_seq = input(f"Enter DNA sequence for '{specieName}': ").strip().upper()

    # Save DNA to file
    try:
        with open(new_file, 'w') as file:
            file.write(dna_seq)
        addSpecie(specieName, new_file)
    except Exception as e:
        print(f"Error writing to file '{new_file}': {e}")

# E) Compare DNA patterns
def compare(specie1, specie2):
    """Compare two species for DNA pattern similarity at same positions (length ≥ 4)."""
    file1 = getFile(specie1)
    file2 = getFile(specie2)

    if file1 == "Specie not found." or file2 == "Specie not found.":
        print("One or both species not found.")
        return

    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            dna1 = f1.read().strip().upper()
            dna2 = f2.read().strip().upper()
    except Exception as e:
        print(f"Error reading files: {e}")
        return

    min_len = min(len(dna1), len(dna2))
    i = 0
    matches = []

    while i < min_len:
        if dna1[i] == dna2[i]:
            start = i
            while i < min_len and dna1[i] == dna2[i]:
                i += 1
            segment = dna1[start:i]
            if len(segment) >= 4:
                matches.append((start, segment))
        else:
            i += 1

    if matches:
        print(f"Similar patterns (size ≥ 4, same positions) between '{specie1}' and '{specie2}':")
        for pos, pattern in matches:
            print(f"Position {pos}: {pattern}")
    else:
        print("No similar patterns of size ≥ 4 at the same positions found.")

# F) Main menu
def main():
    """Display menu and call appropriate functions."""
    while True:
        print("\n--- DNA Species Recognition Menu ---")
        print("1. Print DNA for a species")
        print("2. Add new species")
        print("3. Compare two species")
        print("4. Exit")
        choice = input("Enter your choice (1–4): ").strip()

        if choice == '1':
            sName = input("Enter species name: ").strip()
            file = getFile(sName)
            if file == "Specie not found.":
                print(file)
            else:
                retDNA(file)

        elif choice == '2':
            sName = input("Enter new species name: ").strip()
            addDNA(sName)

        elif choice == '3':
            s1 = input("Enter first species name: ").strip()
            s2 = input("Enter second species name: ").strip()
            compare(s1, s2)

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 1 to 4.")

# Run the program
if __name__ == "__main__":
    main()
