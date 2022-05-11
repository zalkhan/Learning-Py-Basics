import random
#strings can have one or even two perenthesis for example#
print("hello world")
print('more strings')
#you can also use the print function in the same cell/line in jupyter ntbk
print('another string') 
print(3)
#now we woll look at what are variables and how they work
x = 1
#think of it like variables in algebra except in this case the variable is defined already with the given value
#now, lets print said variable
print(x)
#make sure that you don't use parenthesis since that will just print the string not variable 
#a variable can also have the refrence value to a string for instance;
c = "hello"
print(c)
#in python think a variabe being a name tag to a given integer or value
#two or more variables ca have the same namte tag;
d = 2
d = 1
a = 2
print(d)
print(d)
print(a)
#if you change the name tag the original output i.e d now equals 1 is the current value
#you can also assign a variable to another variable
#if you change one of the variables refrence the other variable will remain as the previous value
v1 = 'first string'
v2 = 'second string'
temp = v1
v1 = v2
v2 = temp
print(v1, v2)