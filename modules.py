# modules in python are similar to libraries, files containing code for functions and statements for your program.
# they can be used to import code from other libraries and manage large code into managable code.
import mymodule 
mymodule.greeting('zidane')

x = mymodule.zidane['country']
print(x)

# we can shorten our module namespace

import mymodule as mm
mm.greeting('john')

# There are several built-in modules in Python

# the dir() function is a function that names all variables and functions in a module.
import platform

x = dir(platform)
print(x)
# we can import parts of a module using the 'from' keyword argument.

from mymodule import zidane

print (zidane["age"])