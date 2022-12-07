## SDSS Computing Studies Python Assignment
### Assignment #131 Class Wrapper

Objectives:
* Create a class using class methods
* Use class variables
* Design commands to simplify more complicated tasks

### What is a wrapper?
As you have seen, sometimes there are issues when working with a program, specifically with regard to global and local variables, and making use of handles that are declared outside of program methods.  A class instance is a great way of tying all of these together in the correct scope.  Even better is to create a class that handles more complex tasks that you may be required to use more regularly, and tie them together in one class instance that can be reused on a more regular basis.
In programming we make use of a *wrapper* which is code that wraps around other code components to make accessing them a bit easier. For example, we saw that jquery provides a different way of accessing an object when working with javascript:
```
document.getElementById("item").value = 3
$("#item").val(3)
```
These are functionally the same, but the jquery method is much shorter and easier to enter.  It is code that creates a "nickname" for the first command.  Today we will design a wrapper for sqlite3 connections that we can re-use for other programs.

### Assignment
Open up the file sqlitewrapper.py and look at the class shell. We will use the information in here to help us create generic commands that can be applied to a variety of applications, rather than code that is specific to a single application.
