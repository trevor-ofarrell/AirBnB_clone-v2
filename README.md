# HBNB
# Holberton AirBnB_clone

This is the second step of the Holberton School AirBnB Clone Project.  The goal of this project is to deploy a server with a simple copy of the AirBnB website to demonstrate an understanding (dare we say mastery?) of both front & backend development.

The Final Project Scope Is:

- A command interpreter to manipulate data without a visual interface.
- A website (the front-end) for user interface: static and dynamic
- Data storage through a database or files (i.e. objects)
- An API that communicates between the front-end and the data (retrieve, create, delete, update)

---
## Part 2 (0x02) Requirements
- Impliment Unit Testing in a large project
- Define and use *args and **kwargs
- Handle named arguments in a function
- Create a MySQL database
- Create a MySQL user and grant it privileges
- Understand ORM
- Map a Python Class to a MySQL table
- Handle 2 different storage engines with the same codebase
- Understand and use environment variables

## Part 2 (0x02) Added Functionality
- The def do_create(self, arg): function of the command interpreter (console.py) now allows for object creation with given parameters: Command syntax (create <Class name> <param 1> <param 2> <param 3>...), Param syntax (<key name>=<value>), Value syntax (String: "<value>" => starts with a double quote, Float (<unit>.<decimal> => contains a dot), Integer (<number> => default case).
- Transition to a new MySQL server (new database hbnb_dev_db, new users with specific privilege requirements).
- Updated FileStorage: (models/engine/file_storage.py) with a new public instance method: def delete(self, obj=None): to delete obj from __objects if it’s inside.
- Updated prototype of def all(self) to def all(self, cls=None) that returns the list of objects of one type of class.
- SQLAlchemy is our new best friend!
- Updated BaseModel: (models/base_model.py) to include class attributes: id, created_at, updated_at.
- Moved the models.storage.new(self) from def __init__(self, *args, **kwargs): to def save(self).
- In def __init__(self, *args, **kwargs):, kwargs can now create an instance attribute from the dictionary. (Ex: kwargs={ 'name': "California" } => self.name = "California")
- Removed the key _sa_instance_state from the _dict() method of the class BaseModel
- Added a new public instance method: def delete(self): to delete the current instance from the storage (models.storage) by calling the method delete
- Updated City: (models/city.py) class attributes: name and state_id
- Updated State: (models/state.py) for the name class attribute for DBStorage and FileStorage.
- New engine DBStorage: (models/engine/db_storage.py) with private class attributes (__engine and __session), public instance methods (__init__(self)), dialect: mysql, driver: mysqldb and Environment variables: MySQL user, MySQL password: HBNB_MYSQL_PWD, MySQL host: HBNB_MYSQL_HOST, MySQL database: HBNB_MYSQL_DB.
- Current database session (self.__session) is created from the engine (self.__engine) by using a sessionmaker.
- Updated __init__.py: (models/__init__.py)
- Updated User: (models/user.py)with class attributes: email, password, first_name, last_name, price_by_night, latitude, longitude. Added a relationship with the class Place and Review. 
- 

### Objectives For The BaseModel Class: A Class that defines all common attributes/methods for other classes:

#### Public instance attributes:

- **id:** string - assign with an uuid when an instance is created

- **created_at:** The current datetime when an instance is created

- **updated_at:** The current datetime when an instance is created, updated every time you change your object

- **__str__:** should print: [<class name>] (<self.id>) <self.__dict__>

#### Public instance methods:
- save(self): updates the public instance with the current datetime
- to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance. This method will be the first piece of the serialization/deserialization process to JSON format.

### Objectives For The Command Line Interpreter:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### Operating In Interactive Mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Operating In Non-Interactive Mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
**Example Usage:**
```
newMod = BaseModel()
       - creates an instance of a method

print(NewMod.id)
	- prints the UUID
	   b6a6e15c-c67d-4312-9a75-9d084935e5

print(NewMod.created_at)
         - prints the time when the instance was created (ISO format)
	     '2017-09-28T21:03:54.052298'

print(NewMod.updated_at)
	- prints the most recent time that file was updated (ISO format)
       	  '2017-09-28T21:03:54.052302'
```
### Directory Tree Structure For Phase #1 of HBnB Clone:
```
.
├── AUTHORS
├── console.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── file_storage.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── file_storage.cpython-34.pyc
│   │       └── __init__.cpython-34.pyc
│   ├── __init__.py
│   ├── place.py
│   ├── __pycache__
│   │   ├── amenity.cpython-34.pyc
│   │   ├── base_model.cpython-34.pyc
│   │   ├── city.cpython-34.pyc
│   │   ├── __init__.cpython-34.pyc
│   │   ├── place.cpython-34.pyc
│   │   ├── review.cpython-34.pyc
│   │   ├── state.cpython-34.pyc
│   │   └── user.cpython-34.pyc
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
└── tests
    └── test_models
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-34.pyc
        │   ├── test_amenity.cpython-34.pyc
        │   ├── test_base_model.cpython-34.pyc
        │   ├── test_city.cpython-34.pyc
        │   ├── test_place.cpython-34.pyc
        │   ├── test_review.cpython-34.pyc
        │   ├── test_state.cpython-34.pyc
        │   └── test_user.cpython-34.pyc
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-34.pyc
        │   │   └── test_file_storage.cpython-34.pyc
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py

```
---
## Files

File Name | Description
--- | ---
`README.md` | A description of the Holberton AirBnB Project
`AUTHORS` | A listing of the project contributors
`console.py` | The program to launch the HBNB console
`basemodel.py` | Defines the BaseModel Class
`file_storage.py` | Defines the FileStorage Class & handles the database
`user.py` | Defines the User Class, a subclass of BaseModel
`city.py` | Defines the City Class, a subclass of BaseModel
`state.py` | Defines the User Class, a subclass of BaseModel
`amenity.py` | Defines the Amenity Class, a subclass of BaseModel
`review.py` | Defines the Review Class, a subclass of BaseModel
`place.py` | Defines the Place Class, a subclass of BaseModel
`tests/` | The test directory containing the unittest files for each Class
---

### Commands:
Command Name | Description | Syntax | Example Usage
--- | --- | --- | ---
`Create` | `Create an object` | `create <class name>` | `create BaseModel`
`Show` | `Show an object (based on id)` | `show <class name> <object id>` | `show User my_id`
`Destroy` | `Destroys an object` | ``destroy <class name> <object id>` | `destroy Place my_place_id`
`All` | `Show all objects, of one type or all types` | ``all` or `all <class name>` | `all` or `all State`
`Quit` | `Quit the console` | `quit` or `EOF`
`Help` | `Shows descriptions of commands` | `help` or `help <command>` | `help` or `help quit`
---

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

Contributors:
* **Trevor O'Farrell** - [GitHub - Trevor O'Farrell](https://github.com/trevor-ofarrell) at [Holberton
School](http://holbertonschool.com).
* **Brendan Eliason** - [GitHub - zinczar](https://github.com/zinczar) | [LinkedIn](https://www.linkedin.com/in/brendaneliason/) at [Holberton School](http://holbertonschool.com).