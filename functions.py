# a function is a set of insructions
# functions is a collection of code
def function1():
    print('ahhhhhh')
    print('ahhhhhhh 2')
print('this is outside the function')
# if we are to run this code it would only print outside the function because we didnt command function1 to print function
# now if we just write our function then run the code the function will be executed
function1()
# hope that clears it up 
# a function can also be a mapping
# input or an argument
def function2(x):
    return 2*x
# this means define func2 and take the argument which is X and return the output 2*x
# now lets define x value
a = function2(3)
# this will print 2*3, because as an argument use 3 and call it function2
# now lets try and see if we will get a return value
print(a)
# and it works!!!!
# lets try one more time
b = function2(4)
print(b)
# and our return is 8!!!!
# if we try without an argument value the function and code will not run because there is no argument being made
# this was an example of a function that maps one argument to a return value
# its possible to have multiple arguments in a function
def function3(x, y):
    return x + y
d = function3(1,2)
print(d)
# our return will be 3 because 1 + 2 is equal to 3
# so far we have used functions as a set of code with instructions
# and as a mapping tool
# its possible to combine both!!!!
def function4(y):
    print(y)
    print('still in the function')
    return 3*y
# this says take argument y and print y and the string and then return 3*y to who ever returned the function
f = function4(4)
# if we run this without printing f our argument value, 4 will be printed along with the string  
print(f)
def function5(some_arguments):
    print(some_arguments)
    print('weeeee')
function5(4)
# once we print this we have no return value, only the number 4 and the string 
# even though function 5 has an argument there is no return value.
# BHI calculator
name1 = "Zidane"
height_m1 = 2.2
weight_kg1 = 85

name2 = "Zidane's sister"
height_m2 = 1.5
weight_kg2 = 60

name3 = "Zidane's father"
height_m3 = 2.5
weight_kg3 = 90
def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print('bmi:')
    print(bmi)
    if bmi < 25:
        return name + ' is not overweight' 
    else:
        return name + ' is overweight'
result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)
print(result1, result2, result3)
# once we run this our values will show and printing results will give the conclusion to whether you are or not overweighting
#lets try a quick question to test ourselves!
def convert(miles):
    return 1.6 * miles
print(convert(1))
print(convert(2))
