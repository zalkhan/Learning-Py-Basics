# Booleans represent one of two values: True or False.

# In programming you often need to know if an expression is True or False.

# You can evaluate any expression in Python, and get one of two answers, True or False.

# When you compare two values, the expression is evaluated and Python returns the Boolean answer

# They can be used to evaluate Values, Variables, and Dictionary Values

# Lets revise one way of using Booleans in Python

a = 10
b = 11
if a == 10:
    print (True)
else:
    print (False)

a = 10000
b = 11
if a >= b:
    print ('A is greater than B')

boolean_value = a > b
# when the code is executed it evalutes that A > B but doesn't output because we havent used a print or output function

print(boolean_value)
# This will output true since our value is A>B which is true
# we use boolean_value when preforming complex logic operations
# Lets try this in a function that takes 2 values

def are_you_sad(raining, not_raining):
    if raining == True and not_raining == False:
        return True
    else:
        return False

# We can have the same output with a much simpler and cleaner code

def are_you_sad(is_raining, not_raining):
    return is_raining and not_raining
are_you_sad(True, False)

def are_you_sad(raining, not_raining):
    return not_raining and raining
are_you_sad(False, False)

def c_greater_than_d_plus_e(c, d ,e):
    if c > d + e: 
        return True
    else:
        False

def c_greater_than_d_plus_e(c, d ,e):
    return c > d + e
c_greater_than_d_plus_e(9, 2, 2)