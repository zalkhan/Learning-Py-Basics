class Parent:
    def __init__(self, name, age):
        self.name = 'parent'
        self.age = 32
x = Parent("parent", 32)

class child(Parent):
    pass

class child(Parent):
    def __init__(self, fname, lname):
        self.name = fname
        self.lname = lname
class child(Parent):
  def __init__(self, fname, lname):
    Parent.__init__(self, fname, lname)
class Student(Parent):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    
class Person:
    def __init__(self,fname,lname):
        self.fname = fname 
        self.lname = lname
    def printname(self):
        print (self.fname, self.lname)
class Student(Person):
  pass

x = Student('Mike', 'Wazowski')
x.printname()