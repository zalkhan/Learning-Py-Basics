# as mentioned in the previous file about dictionaries.
# dictionaries are ordered and changeable collection of data.
# they reject duplicate elements.
# they have 2 main components: key value pairs.

thisdict = {
  "brand": "Toyota",
  "model": "Corola",
  "year": 2017
}
print(thisdict)

# we can limit our search by specifying which key we want.

thisdict = {
  "brand": "Toyota",
  "model": "Corola",
  "year": 2017
}
print(thisdict['year'])

# if we have another of the same category/duplicate;
# it will overwrite the existing dict.

thisdict = {
  "brand": "Toyota",
  "model": "Corola",
  "year": 2017,
  "year": 2015
}
print(thisdict)

# another way of accessing specific keys is by using variables.

dict = {
  "brand": "Hyundai",
  "model": "Elentra",
  "year": 2017
}
x = dict["model"]
print(x)

# to get the keys of a dictionary print the following.
x = dict.keys()
# this can be applied to items/key value pairs in the dictionary.

car = {
"brand": "Ford",
"model": "Hummer",
"year": 2020
}

x = car.keys()
y = car.values()

print(x) #before the change

car["color"] = "black"
car["model"] =  "fiesta"

print(x) #after the change
print(y) #after the change

# we can use if statement to determine if there is a key in the dictionary

dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the dictionary")

