# a dictionary in python is sort of like a collection to store data values
# in pairs, similar to an excel sheet but in key-value pairs
# we will be learning how to use dictionaries in python 
d = []
d = dict()
# the code above defines a new dictionary which is currently empty
# here is an example of how a dictionary might look like:
# Ex: d = {"James": 16, "Agnes": 25, "Cameron": 23}
d['Michael'] = 32
# the above says, add a new value pair. Where the key is Michael and the value is 32
d['Agnes'] = 25
d['James'] = 19
# now we have 3 key value pairs!
print (d['Michael'])
# this will print the value associated with the key Michael
# we can also change the value of a key 
d['Michael'] = 38
print (d['Michael'])
# keys are often strings or numbers
# this means we can have both key values as numbers
for key, value in d.items():
    print ('Key:')
    print(key)
    print ('Value:')
    print (value)
    print ('')
    
