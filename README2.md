# AirBnB Clone

This is a command interpreter that manages the objects of the AirBnB clone project. It allows you to manage the objects in a similar manner to the actual AirBnB website.

## Description

The AirBnB clone project entails building a clone of the AirBnB website. It is the first step towards building a full web application with database storage, an API, and front-end integration.

The command interpreter manages the objects of the project. It can:

Create new objects
Retrieve an object from a file
Perform operations on objects
Update attributes of objects
Destroy objects
Command Interpreter Usage
The command interpreter is designed to operate both interactively and non-interactively.

To launch the command interpreter in interactive mode simply run:

$ ./console.py
This will display the prompt (hbnb) indicating you can start typing commands.

Some examples of using the console:


(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) create User
119be863-6fe5-437e-a180-b9892e8746b8
(hbnb) all User
["[User] (119be863-6fe5-437e-a180-b9892e8746b8) {'id': '119be863-6fe5-437e-a180-b9892e8746b8', 'created_at': datetime.datetime(2023, 2, 13, 3, 28, 24, 729889), 'updated_at': datetime.datetime(2023, 2, 13, 3, 28, 24, 729911)}"]
(hbnb) destroy User 119be863-6fe5-437e-a180-b9892e8746b8
(hbnb) quit
Alternatively, the console can be used in non-interactive mode by piping commands into it:


$ echo "help" | ./console.py 
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
$
Documentation
The console handles the following commands:

| Command | Description |
| ---- | ---- |
| create | Creates a new instance of a given class. (Ex: create BaseModel) |
| show | Shows an instance based on id. (Ex: show BaseModel 1234-1234-1234) |
| all | Shows all instances of a given class. (Ex: all BaseModel) |
| destroy | Deletes an instance based on id. (Ex: destroy BaseModel 1234-1234-1234) |
| update | Updates an instance based on id with key/value attributes. |
| quit | Exits the program. |
| EOF | Ends the program. |
| help | Lists all available commands. |
| emptyline | Overrides default empty line behavior and does nothing. |


### Additional documentation for each command is provided via the help command.