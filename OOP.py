# Python is a Object Oriented Programming Language
# Meaning it organizes/functions around
# Data, Objects, etc. 
# A class is a outline for creating a new object
# Lets create one 
class Object:
    def introduce_self(self):
        print('My name is ' + self.name)
# now that we have created an object lets try specifying its features
# like name, color, weight etc...
o1 = Object()
o1.name = 'Object'
o1.color = 'Green'
o1.weight_kg = 50

# FYI, you dont have to call the object as 'object'
# you can name it whatever you like as long as syntax isn't invalid

o1.introduce_self()
# when we execute the code above, it goes back to the function introduce_self then prints the result
# we can output another objects features if it correlates 
# to the function (i.e Introduce_self).

# Be warey if there is a spelling issue when
# specifying attributes of an object 
# as this will result in an attribute error.

# However, the examples above aren't really useful in IRL applications
# There is a pre-defined function called __init__()
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, 
# or other operations that are necessary to do when the object is being created.

class Person:
  def __init__(self, name, age, weight):
    self.name = name
    self.age = age
    self.weight = weight
    

p1 = Person("Zidane", 17, 80, 90)

print(p1.name)
print(p1.age)
print(p1.weight)