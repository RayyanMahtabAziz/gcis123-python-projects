# 🧬 DNA Species Recognition Tool

An interactive Python tool that helps identify, compare, and manage DNA sequences for various species. This project was developed as part of **GCIS-123: Software Development & Problem Solving I @ RIT Dubai**, and demonstrates practical applications of file handling, string manipulation, and biological data analysis.

---

## 📌 Features

- 📄 **Display DNA**: View the DNA strand stored for a specific species.
- ➕ **Add New Species**: Input a new DNA strand and store it in a uniquely named file.
- 🧬 **Compare Two Species**: Detect similar DNA segments (≥ 4 characters) at matching positions.
- 🗃️ **Persistent Storage**: Species and DNA sequences are saved and managed via `.txt` files.
- 🧪 **Menu-Driven Interface**: Allows users to select actions interactively.

---

## 🛠️ Technologies Used

- Python 3
- File I/O and `.txt` manipulation
- Dictionaries for species tracking
- String pattern matching
- Input validation and exception handling

---

## 🚀 How to Run

1. Ensure the following files are in the same directory:
   - `Species Recognition.py`
   - `DNA1.txt`
   - `DNA2.txt`
2. Run the program using:
   ```bash
   python "Species Recognition.py"
