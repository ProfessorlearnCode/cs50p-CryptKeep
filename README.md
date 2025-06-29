
# 🔐 CS50P Final Project: CryptKeep - Encrypted Password Manager (CLI-based)

This is my final project for **Harvard's CS50P: Introduction to Programming with Python**. The project is a simple yet functional **Command Line Interface (CLI) Password Manager** that encrypts and stores your passwords securely using Python and the `cryptography` library.

---

## 🎥 Demo Video

> 🎬 *Coming Soon (Optional)*

---

## 🧠 Project Overview

The **Encrypted Password Manager** allows users to:
- Generate and save **secure encryption keys**
- Create and manage **encrypted password vaults**
- Retrieve saved passwords for specific websites or services
- Run simple interactive commands via the CLI

### 🔒 Key Concepts Demonstrated
- File I/O with Python
- Object-Oriented Programming (OOP)
- CLI-based user interaction
- Symmetric encryption using `cryptography.fernet`
- Secure password handling and persistence

---

## 📂 Project Structure

```

cs50p-CryptKeep/
├── password\_manager.py          # Main application logic
├── test\_password\_manager.py     # Basic testing module
├── requirements.txt             # Required Python packages

````

---

## 🚀 Features

- 🛡️ AES encryption for password storage using `Fernet` (from `cryptography`)
- 🗂️ Store multiple site-password pairs securely in a local file
- 🔑 Key-based encryption and decryption for secure access
- 🧠 Interactive text-based menu for ease of use
- 🧪 Includes basic test file to validate functionality

---

## 💻 Technologies Used

- Python 3.x
- `cryptography` library (`Fernet` encryption)
- CLI (Command Line Interface)
- File I/O operations

---

## 📦 Installation

### 📌 Prerequisites
Make sure you have:
- Python 3.8 or above installed
- `pip` package manager

### 🔧 Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/professorlearncode/cs50p-CryptKeep.git
   cd cs50p-CryptKeep
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the program:**

   ```bash
   python password_manager.py
   ```

---

## 🧩 How It Works

Upon running the script, you'll be presented with an interactive menu:

```text
 What do you want to do?
    1. Create a new key
    2. Load an existing key
    3. Create a new password file
    4. Load existing password file
    5. Add a new password
    6. Get a password
    q. Quit
```

### Example Use Case

1. Generate a new encryption key and store it securely
2. Create a password vault and store initial passwords
3. Load the key and vault later to retrieve or add passwords

All passwords are encrypted before being saved to disk and decrypted only in memory at runtime.

---

## 🧪 Testing

A basic test script (`test_password_manager.py`) is included to verify core functionality like:

* Key creation and loading
* Password encryption/decryption
* File-based persistence

You can extend it using `unittest` or `pytest` for further robustness.

---

## 📝 Notes

* Encryption keys should be stored securely. Anyone with access to the key file can decrypt the stored passwords.
* This project is intended for **educational purposes only** — not recommended for production use without further security hardening.
* Developed as part of the **CS50P curriculum** — to apply core Python concepts in a real-world inspired mini-application.

---

## 🙌 Acknowledgements

* Inspired by the need for basic password management and encryption.
* Thanks to the **CS50 team** and **David J. Malan** for making learning fun and practical.

---

📌 *Feel free to explore, modify, and enhance this project for your own needs!*



