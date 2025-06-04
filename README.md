# 📚 Library Management System

A desktop application built with Python's Tkinter for GUI and MySQL for database management. This system facilitates efficient management of library resources, including books, members, and issue records.

## 🚀 Features

* Add, update, and delete book records
* Manage member information
* Issue and return books
* Search functionality for books and members
* User-friendly graphical interface

## 🛠️ Technologies Used

* **Programming Language:** Python
* **GUI Library:** Tkinter
* **Database:** MySQL
* **Libraries:** `mysql-connector-python, tkinter`

## 📁 Project Structure

The project consists of the following files:

* `Library Management.py`: Main application file that initializes the GUI.
* `Book.py`: Handles book-related operations.
* `Member.py`: Manages member information.
* `Issue.py`: Manages book issuing and returning.
* `Database.py`: Handles database connections and queries.
* `Menulib.py`: Manages the application's menu interface.
* `README.md`: Project documentation.

## 🔧 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Saiff-Tunio/Library-management-system.git
   cd Library-management-system
   ```



2. **Install required libraries:**

   ```bash
   pip install mysql-connector-python
   pip install tkinter
   ```



3. **Set up the MySQL database:**

   * Ensure MySQL is installed and running.
   * Update the database connection details in `Database.py` accordingly.

4. **Run the application:**

   ```bash
   python "Library Management.py"
   ```


## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
