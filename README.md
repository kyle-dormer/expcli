# ExpCli

An expense management tool for the command-line. Using it, you can track your
expenses across days, weeks, months and even years - without ever leaving the terminal.

This program was originally written as the first assignment in the *Introduction to Programming Fundamentals* module of my undergraduate Computing degree.

## Installation
Simply clone the repo into a directory.

### Dependencies
The project has a few dependencies, all of which can be obtained from `pip`.
These are:
* Pandas
* Numpy
* sqlite3

## Usage
To run the program run the command:
```
python3 __main__.py
```

Upon running this command, you will be greeted with a menu of 12 possible options that can be taken. It is recommended to create some categories of expense, add your monthly income sources and add some expenses before attempting to export your expenses.

User data will be stored in an SQLite database in the same directory as the program was cloned to. Likewise, any PDF and CSV exports will also appear there.

To exit the program, simply enter option 12 when prompted to choose an option.
