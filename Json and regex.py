# JSON is a text format that show data in through JS based Object Notation so that transmitting data can be easier and faster.

import json
x =  '{ "name":"Yahya", "age":30, "Country":"Pakistan"}'


y = json.loads(x)

print(y["Country"])

# in the above we parsed (a method where one string of data gets converted into a different type of data.)
# into python data.
# this can be done in revserse fashion as well.

x = {
    'name': 'John Smith',
    'age': '18',
    'car': 'Ford'
}

y = json.dumps(x)
print(y)

import json as json
print(json.dumps(['name:', 'Michael',
                  'age:', 10,
                  'country:', 'USA']))
# this can be done with str, ints, floats, and bools.

#Python to JSON 
#dict -	Object
#list -	Array
#tuple - Array
#str - String
#int - Number
#float - Number
#True - true
#False - false
#None - null

x = {
  "name": "Mike",
  "age": 32,
  "married": False,
  "divorced": False,
  "children": ("Anne", "Billy"),
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

mike = json.dumps(x)

# the result is a JSON string:
print(mike)

# we can format JSON data results with .dumps() with indentation.

x1 = {
  "name": "Mike",
  "age": 32,
  "married": False,
  "divorced": False,
  "children": ("Anne", "Billy"),
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x1, indent=2, separators=(". ", " = ")))
print(json.dumps(x1, indent=4,))
# I forgot to mention that the Sort key method can be done in reverse and sorts either ascending or descending order.
# REGEX:
import re as r
txt = 'regex is cool'
x = r.search('^regex.*cool$', txt)
if x:
    print('Matched')
else:
    print('null')