# a set is a form of data that stores sets
# in python sets reject duplicate elements from a set.

a = set()
a.add(1)
# similar to using append in lists, we can add new elements in sets
print (a)

a.add(2)
print (a)

# a.add(2)
# print (a)
# if we were to execute the code above the set would reject it because
# we already have 2 within our set, and sets reject duplicate elements

for x in a:
    print (x)
    
# sets can be useful at iteration (re-stating elements)

# lets use a set to remove duplicate elements in a given list
given_list = [1, 1, 2, 4, 2]
new_set = set()
for x in given_list:
    new_set.add(x)
print (new_set)

# lets try creating a list that only includes non-duplicate elements from
# our previous list

given_list1 = []
for x in given_list1:
    new_set.append(x)
print (new_set)

# we can also add strings and floats to our sets

b = set()
b.add('hi')
b.add('hey')
b.add('hola')
b.add(1)
print (b)

# you may notice that set has its own order when outputting the
# elements of a list, this is because The order of elements in a set is undefined

given_list2 = [1, 3, 4, 1, 3]
new_set2 = set()
for x in given_list2:
    new_set2.add(x)
total = sum(new_set2)
print (total)

# we can also use the total function similar like we do in forloops
given_list3 = [1, 3, 4, 1, 3]
new_set3 = set()
for x in given_list3:
    new_set3.add(x)
total = 0
for x in new_set3:
    total += x
print (total)

# however, this solution is much longer than required