#we will be learning if-else statements and how they work
x = 1
y = 2
if x < y: 
    print('x is less than y')
#this is an if clause which can contain more code 
a = 1
b = 2
if a < b:
     print ("a is less than b")
     print ("a is definitely less than b")
print ("Not sure if a is less than b")
#its possible to have multiple lines in the same if clause
#because of the indents for the two print functions, the if clause recognizes it
c = 3
d = 4
if c < d:
 print ("c is less than d")
else:
 print ("c is NOT less than d")
 print ("I don't think c is less than d")
print ("outside the if block")
#if you change the value of c then the else statements will be printed on the output
e = 7
f = 8
if e < f:
     print ("e is less than f")
   
elif e == f: 
     print ("e is equal to f")
else:
     print ("e is greater than f")
#same principal follows 
#the single equal sign is a assignment operator whereas double equal sign is equality operator
#we arent assigning but instead evaluating f to e and vice versa
e = 20
f = 8
if e < f:
  print ("e is less than f")
elif e == f:
  print ("e is equal to f")
elif e > f + 10:
  print ("e is greater thanf by more than 10")
else:
  print ("e is greater than f")
#we can have multiple elif conditions and in this case e is greater thanf by more than ten it will print the condition
g = 7
h = 8
if g < h:
  print('g is less than h')
else: 
  if g == h: 
    print('g is equal to h')
  else:
    print('g is greater than h')
#the code above is an example of how you can use if and else statements easily and keeping the code simple.
name = 'zid'
height_m = 2 
weight_kg = 90

bmi = weight_kg / (height_m ** height_m)
print('bmi:')
print(bmi)
if bmi < 30:
  print(name)
  print('is not over weight')
else:
  print(name)
  print('is over weight')