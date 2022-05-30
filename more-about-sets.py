# we can use for loops to reiterate the data in a set
set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for x in set:
    print (x)
    
# we can also print specific elements of a set 
# it will return a bool output if the element is or isnt
# present in the set

print(1 in set)

# like lists we can add items into a set
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set1.add(11)
print(set1)

# we can import set elements from another set using .update
set2 = {"apple", "banana", "cherry"}
set3 = {"pineapple", "mango", "papaya"}

set2.update(set3)

print(set2)

# we can repeat the above without a set as well

set4 = {'hi', 'hello', 'world'}
not_a_set = ['hiyah', 'hey']

set4.update(not_a_set)
print(set4)

# .remove is used to delete element from a set.
set5 = {'green', 'yellow', 'blue'}
set5.remove('green')
print(set5)

# the same is applied with the discard function 

# the clear method empties all elements from a set.

set6 = {'red', 'green', 'purple'}
set6.clear()
print(set6)

# we can conjoin sets with the .union function

set7 = {'pakistan', 'china', 'india'}
set8 = {'america', 'canada', 'mexico'}
set9 = set7.union(set8)
print (set9)

# using the intersection_update function we can return element that are
# present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# symmetric_difference_update does the opposite 