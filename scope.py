# a Python scope determines where in your program, a name is visible. Python scopes are implemented as dictionaries that map names to objects.
# there are 4 main types of scopes: GlobalScope, LocalScope, BuiltinScope and EnclosingScope.

# local variables are variables created inside a function and only used in said function. 

def function():
    x = 1
    print (x)
function()

# however, we can still use a local variable within the function of the function
def function():
    x = 1
    def infunction():
        print (x)
    infunction()
function()

# global variable are variables created outside a function or in the main body code.
# global variables are available from within any scope, global and local.

x = ('hi')
def newfunctions():
    print(x)
newfunctions()

print(x)

# using the same variable for both scopes will cause the interpreter to seperate the variable as 2 different things.
# the local will be outputted first, the global will be outputted second.

x = ('hi')
def anotherfunctions():
    x = ('hello')
    print (x)
anotherfunctions()
print(x)

# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.

def newglobal():
    global x
    x = ("namaste")
newglobal()
print(x)

# we can use the global keyword if we want to make a change to a global variable inside a function.
# To change the value of a global variable inside a function, refer to the variable by using the global keyword

# Enclosing scope is also known as non-local scope. They refer to the names of a variable defined in the nested function. 

def my_message():
    message = "python!" # A nonlocal variable
    def nested():
        nonlocal message  # Declare var as nonlocal
    nested()
    print(message)
my_message()  


# When the variable or object is not found in local, global, or enclosing scope, then Python starts looking for it in the built-in scope. 
# Built-in scopes are one of the widest scopes that cover all the reserved keywords. 
# These are easy to call anywhere in the program prior to using them, without the need to define them.