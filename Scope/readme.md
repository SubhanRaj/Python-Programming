# Scope in Python

* In python scope is the region from where a variable is accessible.
* There are two types of scope in python:
    * Global scope
    * Local scope
* In Python, local and global scopes refer to different parts of a program where variables are accessible.
  
## Local Scope and Variables

* Local scope refers to the part of the program where variables are defined within a function. These variables are accessible only within the function.
* Local scope refers to the part of the program where variables are defined within a function. These variables are accessible only within the function.
* Local variables cannot be accessed outside of the function.
* Example:
```python
def my_function():
    x = 10  # Local variable
    print(x)  # Output: 10

my_function()
print(x)  # Raises NameError: name 'x' is not defined
```

## Global Scope and Variables

* Global scope refers to the part of the program where variables are defined outside of a function. These variables are accessible throughout the program.
* Global variables can be accessed and modified by any function or code block within the program.
* Global variables are created when they are first assigned a value and persist until the program terminates.
* Example:
```python
x = 10  # Global variable

def my_function():
    print(x)  # Output: 10

my_function()
print(x)  # Output: 10

```

## Forcing Global Scope 
* By default, variables defined within a function have local scope and shadow any variables with the same name in the global scope.
* To force a variable in a function to refer to the global variable with the same name, we can use the global keyword before the variable name.
* Example:
```python
x = 10  # Global variable

def my_function():
    global x  # Refer to the global variable
    x = 20  # Modify the global variable
    print(x)  # Output: 20

my_function()
print(x)  # Output: 20

```
* In the example above, the global keyword is used to indicate that the variable x in the function refers to the global variable x. Any modifications made to the variable x within the function will affect the global variable.