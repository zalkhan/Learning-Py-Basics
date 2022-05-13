# Recap
# In the last session we worked on forloops and how to retrieve data from a given range using an If operator whith our for loop
total = 0
for i in range(1,5):
    total += i
    print(total)
# we can do the same using a while loop 
total2 = 0
j = 1
while j < 5:
    total2 += j
    j += 1
print(total2)
# what the code above says is that:
# once we run our while loop, check if it is less than 5
# if true, then add variable J with our total then add J by 1
# we can use while loops even if we dont know how many loops we need for a given range
given_list = [5 , 4 , 4 , 3 , 1 , -2 , -3, -5]

total3 = 0
i = 0
while given_list [i] > 0:
    total3 += given_list[i]
    i += 1
print(total3)
# what the code above is saying is, starting from 0, if it is more than 0 then add our current element with total3
# after that move to the next item from the list, hence (i += 1)
# if we tried running with all positive numbers then it would result in a index error
# This is because python will interpret it as index 5 instead of index 0 
# hope that made sense lol
given_list = [5 , 4 , 4 , 3 , 1 , -2 , -3, -5]

total3 = 0
i = 0
while i < len(given_list) and given_list[i] > 0:
    total3 += given_list[i]
    i += 1
print(total3)
# the len operator is a built-in operator that sees the length of a given index, string, array, list, etc.
# lets try using a for loop
given_list2 = [5 , 4 , 4 , 3 , 1 , -2 , -3, -5]
total4 = 0
for element in given_list2:
    if element <= 0:
        break
    total4 += element
print(total4)
# We used a break statement to cancel out our negative numbers with our for loop
given_list4 = [7, 5 , 4 , 4 , 3 , 1 , -2 , -3, -5, -7]
total5 = 0
for element in given_list4:
    if element >= 0:
        break
    total5 += element
print(total5)