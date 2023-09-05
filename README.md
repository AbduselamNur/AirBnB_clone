#	`0x00. AirBnB clone - The console`


#### Group project | Python | OOP

============================================================================
	COLLABORATIOM WITH
		* Zekaria Mohammed
		* Abduselam Nurhussen

### `General Description`

* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

### `The console`

* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

### `Command Interpreter`

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

### Execution

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):

========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
