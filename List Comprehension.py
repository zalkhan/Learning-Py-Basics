a = [1, 3, 5, 7, 9, 11]

# lets say we want to join two lists as one, we could append, add or extend them

# b = [2, 6, 10, 14, 18, 22] 
#for x in b: 
  #a.append(x)

#print(a)

#a.extend(b)
#print(a)

# lets try another approach

c = [x * 2 for x in a]
print(c)
# This will run the same as above but much simpler and cleaner syntax

d1 = []
for x in range(1, 7):
    d1.append(x ** 2)
print(d1)

d2 = [x ** 2 for x in range(1,7)]
print(d2)

[36, 25, 16, 9, 4, 1]
for x in range(6, 0 , -1):
    print(x)

e1 = []
for x in range(6, 0 , -1):
    e1.append(x**2)
print(e1)

e2 = [x**2 for x in range(6, 0 , -1)]
print(e2)

e4 = []
e4 = [x ** 2 for x in reversed(range(1, 7))]
print(e4)

