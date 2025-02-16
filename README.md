# Password Generator & Manager

A simple desktop application built with Python and Tkinter that allows users to generate strong random passwords, save them securely in a SQLite database, and view their saved passwords.

## Features

- **Generate Strong Passwords**: Automatically generates a random password with a combination of letters, digits, and special characters.
- **Save Passwords**: Save your website credentials (website, username, and password) securely in a local SQLite database.
- **View Saved Passwords**: View all your saved passwords in a clean and organized interface.
- **User-Friendly GUI**: Easy-to-use graphical user interface for managing your passwords.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Required Python libraries: `tkinter`, `sqlite3`, `random`, `string`.

### Steps to Run the Application

1. **Clone or Download the Code**:
   - Clone this repository or download the source code files.

2. **Install Dependencies**:
   - Ensure you have Python installed. You can download it from [here](https://www.python.org/downloads/).
   - The required libraries (`tkinter`, `sqlite3`, etc.) come pre-installed with Python.

3. **Run the Application**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the following command:
     ```bash
     python password_manager.py
     ```
   - The application window will open, and you can start using it.

## Usage

1. **Generate a Password**:
   - Enter the website name and username in the respective fields.
   - Click the "Generate Password" button to generate a strong random password.
   - The generated password will automatically appear in the password field.

2. **Save a Password**:
   - After generating or manually entering a password, click the "Save Password" button.
   - A confirmation message will appear if the password is saved successfully.

3. **View Saved Passwords**:
   - Click the "View Saved Passwords" button to open a new window displaying all your saved credentials.
   - If no passwords are saved yet, a message will indicate that.

4. **Clear Fields**:
   - After saving a password, the input fields will be cleared automatically for convenience.

## Database

The application uses a SQLite database (`password_manager.db`) to store your credentials. The database file will be created automatically in the same directory as the script when you run the application for the first time.

### Table Structure

The database contains a single table named `passwords` with the following columns:
- `id`: Auto-incrementing primary key.
- `website`: The name of the website.
- `username`: The username or email associated with the website.
- `password`: The password for the website.

## Security Note

This application is intended for educational purposes and personal use. It does not implement advanced security measures such as encryption. For enhanced security, consider using a more robust password manager with encryption features.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to fork the repository and submit a pull request.
---

Made Gaurav Chauhan
