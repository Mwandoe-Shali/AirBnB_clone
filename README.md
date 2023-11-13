# Project: 0x00. AirBnB clone - The console

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


## Resources

#### Read or watch:

* [cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A)
* [cmd module in depth](https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg)
* [packages concept page]()
* [uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ)
* [datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA)
* [unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)
* [args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)
* [Python test cheatsheet](https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw)
* [cmd module wiki page](https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ)
* [python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA)
## Learning Objectives

### General

* How to create a Python package
* How to create a command interpreter in Python using the <code>cmd</code> module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage <code>datetime</code>
* What is an <code>UUID</code>
* What is <code>*args</code> and how to use it
* What is <code>**kwargs</code> and how to use it
* How to handle named arguments in a function
## Tasks

| Task | File |
| ---- | ---- |
| 0. README, AUTHORS | [SOON](./) |
| 1. Be pycodestyle compliant! | [SOON](./) |
| 2. Unittests | [SOON](./) |
| 3. BaseModel | [SOON](./) |
| 4. Create BaseModel from dictionary | [SOON](./) |
| 5. Store first object | [SOON](./) |
| 6. Console 0.0.1 | [SOON](./) |
| 7. Console 0.1 | [SOON](./) |
| 8. First User | [SOON](./) |
| 9. More classes! | [SOON](./) |
| 10. Console 1.0 | [SOON](./) |
