# a tuple is a data type to store multiple items in a variable.
# this type of data is unchangable.
# for example:
x = ('hi', 'hello', 'hey')
print (x)

# tuples are stored in ordered fashion.
# tuples also allow duplicate values.
# tuple are indexed starting from 0.

x = ('hi', 'hello', 'hey')
# take a look at the input of var X, its ouput is the same.
# when we say ordered it means our order is defined from our code.
# you cannot add or remove items if a tuple has already been created.
# since they are indexed they can share an index with the duplicate values.


x = ('hi', 'hello', 'hey')
print(len(x))

# using the len operator we can see the number of words in our tuple.
# to avoid confusion, remeber a tuple will contain a comma to singify it is indeed a tuple.
# for example:
x = ('hi',)
print (type(x))
# this is a tuple
y = ('hi')
print(type(y))
# this is not a tuple
# tuples can contain any data type.
tuple = ("apple", "banana", "cherry")
tuple1 = (1, 5, 7, 9, 3)
tuple2 = (True, False, False)

# we can also use these different types of data in a tuple.
tuple3 = ("hi", 34, True, 40, "male")

# tuple constructors can also be used to create a tuple.
thistuple1 = (("apple", "banana", "cherry"))
print(thistuple1)


# Acessing tuples:
# You can access tuple items by referring to the index number, 
# inside square brackets:

tuple = ("apple", "banana", "cherry")
print(tuple[2])

# as previosuly mentioned our index starts from 0.
# the output of the tuple will be 'cherry'
# we can also use negative index to indicate the last or second to last.
tuple = ("apple", "banana", "cherry")
print(tuple[-2])

# we can use ranges to specify the start and end of the tuple
tuple = ("apple", "banana", "cherry")
print(tuple[0:1])
# or
tuple = ("apple", "banana", "cherry")
print(tuple[:1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the end item/position is not included.
# if we dont include an end position, our tuple keeps returning till
# the end of the tuple

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# we can use a similar approach with negative indexing.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:-1])

# we can check if we have a element in our tuple using an if statement with the print function.
# previosuly I meantioned that tuples cannot be changed but,
# we can convert them
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = y
print(x)

# now that we have converted our tuple into a list we can add/append
# elements into the list.

x1 = ("apple", "banana", "cherry")
y1 = list(x)
y1.append ("orange")

def convert(x1):
    return tuple(x1)
print(x1)

# we can add a tuple(s) into another tuple using the += operator

tuple1 = ('a', 'b', 'c', 'd', 'e', 'f')
tuple2 = ('g', 'h', 'i', 'j', 'k', 'l')
tuple1 += tuple2
print (tuple1)

# to remove items/elements from a tuple we can use coversion
# like in the above, but I wont be including that.
# when adding values into a tuple we call this packing.
# we can also do something called unpacking that
# returned the values into variables.

f1 = ('hi', 'lo', 'mo')
(a, b, c) = f1
print(a, b, c)
# or
print(a)
print(b)
print(c)

# if we have less variables than values, using asterisk/* we can 
# put the remainder of unassingmed variables into a list



fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)