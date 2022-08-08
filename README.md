# AirBnB clone - The console

## Desciption of the project

This is the first step towards building a first full web application: the AirBnB clone.
The goal of the project is to deploy on your server a simple copy of the [AirBnB website](https://www.airbnb.com/).

## Command line interpreter

A command interpreter is to be used to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

## The console

- Create a data model
- Manage (create, update, destroy, etc) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give an abstraction between “My object” and “How they are stored and persisted”. This means: from the console code (the command interpreter itself) and from the front-end and RestAPI (to be built later), there would be no need to pay attention or take care of how the objects are stored.

This abstraction will also allow changing the type of storage easily without updating all of the codebase.

The console will be a tool to validate this storage engine.

## Files and Directories
- *models* directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- *tests* directory will contain all unit tests.
- *console.py* file is the entry point of the command interpreter.
- *models/base_model.py* file is the base class of all the models. It contains common elements:
   - attributes: *id*, *created_at* and *updated_at*
   - methods: *save()* and *to_json()*
- *models/engine* directory will contain all storage classes (using the same prototype). Only file_storage.py for now.

## Storage

Persistency is really important for a web application. It means: every time the program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database.

Separating “storage management” from “model” makes the models modular and independent. With this architecture, the storage system  can easily be replaced without re-coding everything everywhere.

Class attributes will always be used for any object and not instance attributes For 3 reasons:

- Provides easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)
- Provides default value of any attribute
- Provides the same model behavior for file storage or database storage

## Commands

* all
The __all__ command will retrieve the string representation of all the models in the file storage
