# lets recap what we learnt previosuly
class person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
p1 = person('Zidane', 20, 'pakistan')
print (p1.name)
print (p1.age)
print (p1.country)

# we learned how to create a class using the pre defined init function
# how to define a class attributes with 'self'
# as well as using a introduction with our class once executed

class Person:
    def introduce_self(self):
        print ('my name is ' + self.name)
        
po1 = Person()
po1.name = 'Zidane'
po1.age = 20
po1.country = 'pakistan'

po1.introduce_self()

# lets create a new class while using boolean operators (True and False).

class Person:
    def __init__(self, N, P, I):
        self.name = N
        self.age = P
        self.race = I
    def sitdown(self):
        self.is_sitting = True
    def standup(self):
        self.is_sitting = False
pe1 = Person("zidane", 'introverted', True)
pe2 = Person("laiba", 'extroverted', False)

pe1.person_owned = po1
# the above means pe1 owns p1

pe1.person_owned.introduce_self()
# the would execute the owned class (p1) even though it is owned by pe1
