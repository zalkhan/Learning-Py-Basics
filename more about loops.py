# lets recap our previosu sessions
a = ["apple", "banana", "republic"]
for element in a:
    print (element)

# we learned how to use forloops and while loops in a given variable or list.
for i in range (len(a)):
    print (a[i])
    
# in some cases our index might be more important than the element

for i in range (len(a)):
    for j in range(i + 1):
        print (a[i])

# what the 2nd for loop is saying is, while i = 0, j will already be 0
# then when i is 1, j will be 0, 1 and so on.

total1 = 0
for i in range(1,100):
    if i % 3 == 0 or i % 5 ==0:
        total1 += i
print (total1)

given_list4 = [7, 5 , 4 , 4 , 3 , 1 , -2 , -3, -5, -7]
total2 = 0
j = len(given_list4) - 1
while given_list4[j] < 0:
    total2 += given_list4[j]
    j -= 1
print(total2)


