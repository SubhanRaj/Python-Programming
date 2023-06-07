# Functions in Python

* Functions are a block of code which only runs when it is called.
* You can pass data, known as parameters, into a function.
* A function can return data as a result.
* In Python a function is defined using the def keyword.
* There are two types of functions:
  * Built-in functions
  * User-defined functions

## Built-in functions

* Built-in functions are the functions which are already defined in Python.
* These functions are ready to use.
* Built-in functions are also called pre-defined functions.
* Following is the list of some important built-in functions in Python along with their description:

| Function | Description |
| --- | --- |
| `input()` | This function is used to take input from the user. |
| `print()` | This function is used to print something on the screen. |
| `type()` | This function is used to find the type of the variable. |
| `int()` | This function is used to convert a variable into an integer. |
| `float()` | This function is used to convert a variable into a float. |
| `str()` | This function is used to convert a variable into a string. |
| `len()` | This function is used to find the length of a string. |
| `range()` | This function is used to generate a sequence of numbers. |
| `list()` | This function is used to convert a sequence into a list. |
| `tuple()` | This function is used to convert a sequence into a tuple. |
| `dict()` | This function is used to convert a sequence of tuples into a dictionary. |
| `set()` | This function is used to convert a sequence into a set. |
| `abs()` | This function is used to find the absolute value of a number. |
| `sum()` | This function is used to find the sum of all the elements in a list. |
| `max()` | This function is used to find the maximum value in a list. |
| `min()` | This function is used to find the minimum value in a list. |
| `sorted()` | This function is used to sort a list. |
| `reversed()` | This function is used to reverse a list. |
| `all()` | This function returns True if all the elements in a list are true. |
| `any()` | This function returns True if any of the elements in a list is true. |
| `enumerate()` | This function is used to add a counter to an iterable. |
| `zip()` | This function is used to zip the two lists. |
| `map()` | This function is used to apply a function to all the elements in a list. |
| `filter()` | This function is used to filter the elements in a list. |
| `lambda()` | This function is used to create an anonymous function. |

## User-defined functions

* In Python we can create our own functions which are called user-defined functions.
* User-defined functions are defined by the user.
* User-defined functions are also called custom functions.
* Following is the syntax of a user-defined function:

```python
def function_name(parameters):
    """docstring"""
    statement(s)
    return value
```

* In the above syntax:
  * `def` is a keyword which is used to define a function.
  * `function_name` is the name of the function.
  * `parameters` are the parameters of the function.
  * `docstring` is the description of the function.
  * `statement(s)` are the statements which are executed by the function.
  * `return` is a keyword which is used to return a value from the function.
  * `return value` is the value which is returned by the function.
  
* Example:

```python
def add(a, b):
    """This function adds two numbers"""
    return a + b
```
### Rules for user-defined functions

* Function blocks begin with the keyword `def` followed by the function name and parentheses ().
* Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
* The first statement of a function can be an optional statement - the documentation string of the function or docstring.
* The code block within every function starts with a colon (:) and is indented.
* The statement `return [expression]` exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.
* A function can return multiple values separated by commas.
* A function can also be called using keyword arguments of the form `kwarg=value`.
* A function can also be defined with a variable number of arguments using the following syntax:



