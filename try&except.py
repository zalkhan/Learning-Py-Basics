'''
The 'try' block lets you test a block of code for errors.

The 'except' block lets you handle the error.

The 'else' block lets you execute code when there is no error.

The 'finally' block lets you execute code, regardless of the result of the try- and except blocks.
'''
try:
    x = 1
    print(x)
except:
    print('an error occurred')
else:
    print('no error occurred')
    
# if x were undefined our error message would've been executed.

# we can use except function numerous times to specify different areas of testing.
# like testing NameError for one space of code and another test for another space of code.

try:
    print(y)
except NameError:
    print('Undefined Var')
except:
    print('error occured')
    
### You can use the else keyword to define a block of code to be executed if no errors were raised:


#### The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
    z = open('inheritance comments.txt')
    try:
        z.write('hello')
    except:
        print('Could not write')
    finally:
        z.close()
except:
    print('something went wrong')
    
# raise exceptions:
a = -29
if a < 0:
    raise Exception('Not Calculable')
