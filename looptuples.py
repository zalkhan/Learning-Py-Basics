# like lists, we can iterate through values using for loop with our tuple
tuple = ('a', 'b')
for i in tuple :
    print (i)

# we can do the same by iterating our index values using
# the range and len operators.

tuple = ('a', 'b')
for x in range(len(tuple)):
    print(tuple[x])
    
# lets try using a while loop
tuple = ('a', 'b')
i = 0
while i < len(tuple):
    print(tuple[i])
    i = i + 1
    
