# 0x00. AirBnB clone - The console
`Group project` `Python` `OOP`

This is a group project of two, that aims at clone the AirBnB web app.
The project uses Python language as it utilizes it's Object Oriented Programming
structure.

## Background Context
**First step: Write a command interpreter to manage your AirBnB objects.**

This is the first step towards building your first full web application: the AirBnB clone.
This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:
* put in place a parent class `BaseModel` to take care of the initialization, serialization & deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (`User`, `State`, `City`, `Place`, ...) that inherit from `BaseModel`
* create the first abstracted storage engine of the project: **File storage**
* creae all unittests to validate all our classes and storage engine

### What's a command interpreter?
It's xactly the same as Shell but limited to a specific use-case.
In our case, we want to be able to manage the objects of our project:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Resources
**Read or watch:**
* [cmd module](https://docs.python.org/3.8/library/cmd.html)
* [cmd module in depth](pymotw.com/2/cmd/)
* [Python packages](https://intranet.alxswe.com/concepts/66)
* [uuid module](https://docs.python.org/3.8/library/uuid.html)
* [datetime](https://docs.python.org/3.8/library/datetime.html)
* [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
* [cmd module wiki page](https://wiki.python.org/moin/CmdModule)
* [python unittest](https://realpython.com/python-testing/)

## Learning Objectives
### General
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is `*args` and how to use it
* What is `**kwargs` and how to use it
* How to handle named arguments in a function

![Image representation of the project's framework flow](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231009%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231009T100835Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=67dec202b19ecceb750bacd83cc9134ff75c8390bf8b255d376091c78618268d)
