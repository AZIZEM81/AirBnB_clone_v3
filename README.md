AirBnB Clone - The Console
The console is the first segment of the AirBnB project at Holberton School, which covers fundamental concepts of higher-level programming. The goal of the AirBnB project is to eventually deploy a server as a simple copy of the AirBnB website (HBnB). In this segment, a command interpreter is created to manage objects for the AirBnB (HBnB) website.

Functionalities of this command interpreter:
Create a new object (e.g., a new User or a new Place)
Retrieve an object from a file, a database, etc.
Perform operations on objects (e.g., count, compute stats)
Update attributes of an object
Destroy an object
Table of Contents
Environment
Installation
File Descriptions
Usage
Examples of Use
Bugs
Authors
License
Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using Python 3 (version 3.4.3).

Installation
Clone this repository:

bash
Copier le code
git clone "https://github.com/AZIZEM81/AirBnB_clone_v3.git"
Access the AirBnB directory:

bash
Copier le code
cd AirBnB_clone_v3
Run the command interpreter interactively:

bash
Copier le code
./console
Enter your command in the console.

Run the command interpreter non-interactively:

bash
Copier le code
echo "<command>" | ./console.py
File Descriptions
console.py - Contains the entry point of the command interpreter. The console currently supports the following commands:

EOF - Exits the console.
quit - Exits the console.
<emptyline> - Overrides the default empty line method and does nothing.
create - Creates a new instance of BaseModel, saves it to the JSON file, and prints the id.
destroy - Deletes an instance based on the class name and id, saving the change into the JSON file.
show - Prints the string representation of an instance based on the class name and id.
all - Prints the string representation of all instances, optionally filtered by class name.
update - Updates an instance based on the class name and id by adding or updating attributes, saving the change into the JSON file.
models/ directory contains classes used for this project:
base_model.py - Defines the BaseModel class from which other classes are derived:

def __init__(self, *args, **kwargs) - Initialization of the base model.
def __str__(self) - String representation of the BaseModel class.
def save(self) - Updates the attribute updated_at with the current datetime.
def to_dict(self) - Returns a dictionary containing all keys/values of the instance.
Classes inherited from BaseModel:

amenity.py - Contains the Amenity class, derived from BaseModel.

