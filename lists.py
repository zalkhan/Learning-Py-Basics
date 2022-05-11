# #lists are a type of data structure that can store lists
# ln 2 means define a new list with the given value and/or items
# now our list should be created and output to our terminal
# we can also add a new element to our list using the append operator
a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.append(b)

print(a)

c = [3, 10, -1]
print(c)
c.append(1)
print(c)
#in the first 3-4 lines we used lists containing strings and then next 4 using intergers.
c.append('hello')
print(c)
c.append([1,2])
print(c)
# ln 20, 21 means is that in the existing list we added another list
# this can be implimented in data science FYI
c.pop()
print(c)
# the pop function is a pre defined function that removes the last element of a list
print(c[0])
# in python we can also retrieve a specific bit of data using the function in the above
# also items in lists or namely python start from zero, since 3 is our first digit its index is 0
# we can also alter/modify our existing lists by assigning a new index or value to a specific
c[0] = 5
print(c)
b = ['banana', 'apple', 'microsoft']
b[0] = 'microsoft'
b[2] = 'banana'
print(b)
#there are a variety of ways we can switch between different data in strings, we can use the temp function or use our index's in similar scenarios
