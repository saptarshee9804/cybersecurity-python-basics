# Cybersecurity Python Basics 🔐

A beginner-friendly collection of Python projects and cybersecurity exercises developed while learning Python programming, cryptography, and digital forensics.

## 📌 Projects

### 1. Password Checker
A simple Python program that evaluates basic password characteristics.

**Features**
- Checks password length.
- Checks for uppercase and lowercase letters.
- Checks for digits and special characters.
- Provides a basic feedback category.

**File:** `password_checker.py`

### 2. File Integrity Checker Using SHA-256
A Python tool that calculates a file's SHA-256 hash and checks whether its contents have changed compared with a previously saved hash.

**Features**
- Calculates SHA-256 hashes.
- Saves an original hash in a JSON record.
- Compares subsequent hashes against the saved record.
- Reports whether the file matches the recorded fingerprint.

**File:** `file_integrity_checker.py`

## 🛠️ Technologies Used

- Python 3
- SHA-256 hashing
- JSON
- Git and GitHub

## 🚀 Getting Started

### Prerequisites
- Python 3 installed on your computer.

### Run the Password Checker

```bash
python password_checker.py
```

### Run the File Integrity Checker

1. Create a test file named `sample.txt` in the project folder.
2. Run:

```bash
python file_integrity_checker.py
```

3. Enter `sample.txt` when prompted.
4. On the first run, the program saves the original hash.
5. Run it again to verify the file against the saved hash.
6. Modify the file and run the program again to test change detection.

## 📚 Learning Objectives

- Practise Python functions and conditional statements.
- Understand SHA-256 hashing.
- Learn file handling and JSON storage.
- Explore file integrity verification concepts.
- Practise using Git and GitHub to manage source code.

## ⚠️ Limitations

These are educational projects. The password checker uses basic rules and does not guarantee password security. The file integrity checker relies on a saved hash record, which must be protected independently for trustworthy verification.

## 👨‍💻 Author

Cybersecurity student learning Python programming, cryptography, and digital forensics.

---

*This repository is a learning project and will be improved as new skills and features are developed.*
