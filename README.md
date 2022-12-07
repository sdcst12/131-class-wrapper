## SDSS Computing Studies Python Assignment
### Assignment #130 Class Methods

Objectives:
* Create a class using class methods
* Use class variables

We have considered splitting code up into different programs, and then passing information between them using API calls.  A similar kind of modularity is set up within a single program using classes and class instances.

We can think of a class as a template for an object, that has its own variables, data and functions that can make use of its data.  We can create multiple instances of that class template by *instantiating* that class template, and then we can actually store data in its variables and use it as an object.

Classes that are created with only static methods are great for organizing.  You don't have to worry about conflicting variable names from other parts of your code, because all of the methods/functions that are defined in the class are confined to the class.

Although it's possible to create a class with static or class based methods and not bother with instantiating your class, it's just as simple to create an instances of your object.

Important notes:

1. A class is just a template until it is *instantiated*. This means assigning it to a variable that will act as its handler.  This is simply done by assigning it to a variable.  All references to class variables and methods will use the handler.  Note that we can use any name, or even a list or dictionary element.  In this way, we can actually have multiple instances of the object:
```
class connections:
  *code here*

app = connections

conns = []
conns.append(connections)
```

2. Two important class methods are the constructor (__init__) and destructor (__del__) methods.  The constructor is called when the class is instantiated, and any parameters are passed to the constructor to be used.  This is a great way of setting initial values in the constructor.  The destructor is called when the object is destroyed, which also happens when the program terminates. It is not especially important for us yet, but becomes very important for the release of memory back to the program if an instance is destroyed and the program continues to run.  Consider a server that handles multiple incoming connections. Each connection would be a class instances.  When the connection is terminates, we don't need to keep any information about the connection anymore, so it can be destroyed

3.  All class methods must include the default parameter *self*.  This allows each class method to access the class variables and methods.

4.  Within the class, we can access class properties and methods using dot notation.  For example, the class property *variable1* would be accessed as *self.variable1*, and the class method *add()* would be accessed as *self.add()*

5.  While it is possible to set class properties using simple variable assignment, it is better to create a method that handles such operations:
```
direct assignment of class properties
object.variable1 = 10
```
```
assignment of class property using class method
object.set('variable1',10)
```

** Assignment
Although we have done this before, we will be creating a version of tic-tac-toe that operates entirely with a class instance.  The purpose of this assigment is to become familiar with class objects and instances and start thinking about working within a class.

** Bonus
Interested in improving the appearance of your program? Consider the use of ANSI code.
Even more challenging is the use of Curses module:
https://pypi.org/project/windows-curses/
https://docs.python.org/3/howto/curses.html

