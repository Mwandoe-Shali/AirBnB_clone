# AirBnB Clone Project

## Project Description

This project aims to create a simplified version of the AirBnB web application, focusing on building a command-line interface to manage AirBnB objects. The project involves creating a parent class (BaseModel) for object initialization, serialization, and deserialization. It also includes implementing a flow of serialization/deserialization, creating various classes for AirBnB objects, and developing a file storage engine. The command interpreter allows users to perform operations such as creating, retrieving, updating, and destroying objects.

## Command Interpreter

### How to Start

To start the command interpreter, run the following command in the terminal:

bash
Copy code
./console.py
### How to Use

Once the command interpreter is running, you can use the following commands:

help: Display a list of available commands.
quit or EOF: Exit the command interpreter.
Additional commands related to managing AirBnB objects will be added as the project progresses.

### Examples

Interactive Mode:

bash
Copy code
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) quit
$
Non-interactive Mode:

bash
Copy code
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
Remember to consult the help command within the interpreter for detailed information on available commands and their usage.

## Requirements

Python 3.8.5
pycodestyle (version 2.8.*)

## Unit Tests

To run unit tests, use the following command:

bash
Copy code
python3 -m unittest discover tests
Make sure to follow the file organization in the tests folder, matching the structure of your project.