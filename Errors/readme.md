# Errors and Error Handling in Python

* An error is a problem in a program that prevents the program from running as expected.
* When the interpreter encounters an error, it stops execution of the program and prints an error message.
* Python has many built-in error types that are raised when the interpreter encounters an error.
* Errors can be both made by the developers as well as the users.
* The errors made by the developers can be identified and fixed by the developers themselves during the development phase.
* While we didn't need what the user will do, so we need to handle the errors made by the users.
* This is called error handling.
* We'll first look at the different types of errors in python and then we'll look at how to handle them.

## Errors in Python
* Errors occur due to multiple reasons, such  as: erros in syntax, errors in logic, errors in indentation, etc.
* In python there are two types of errors: syntax errors and logical errors(exceptions).
  
### Syntax Errors

* In python syntax errors occur when there is anything wrong with the syntax of the program.
* Syntax errors are also known as parsing errors.
* Syntax errors can be detected by the Python interpreter.
* Following are some examples of syntax errors:

```python
# Example 1
print("Hello World!) #This is  syntax error as there is a missing double quote at the end of the string.
# Output
    File "<ipython-input-1-9b8b6b0b0e2a>", line 1
        print("Hello World!)
                            ^ SyntaxError: EOL while scanning string literal # EOL: End of Line

# Example 2
if (a > b)      # This is a syntax error as there is no colon at the end of the if statement.
    print("a is greater than b") 
# Output
    File "<ipython-input-2-9b8b6b0b0e2a>", line 1
        if (a > b)
                  ^
    SyntaxError: invalid syntax
```

### Logical Errors

* Logical errors are also known as exceptions.
* They occur when the program is syntactically correct but the code results in an error. 
* These errors are detected while the program is running.
* There are several types of logical errors in python, which ranges from incorrect type conversion, incorrect indentation, incorrect arithmetic operations, wrong use of methods and functions, division by zero, searching for a non-existent key in a dictionary, wrong indexing of a list, etc.
* Following are some examples of logical errors:

```python
# Example 1
a = 10
b = 0
print(a/b) # This is a logical error as we cannot divide a number by zero.

# Output
    ---------------------------------------------------------------------------
    ZeroDivisionError                         Traceback (most recent call last)
    <ipython-input-3-9b8b6b0b0e2a> in <module>
          1 a = 10
          2 b = 0
    ----> 3 print(a/b) # This is a logical error as we cannot divide a number by zero.

    ZeroDivisionError: division by zero

# Example 2
a = 10
b = "Hello"
print(a+b) # This is a logical error as we cannot add a number and a string.

# Output
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-4-9b8b6b0b0e2a> in <module>
          1 a = 10
          2 b = "Hello"
    ----> 3 print(a+b) # This is a logical error as we cannot add a number and a string.

    TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Example 3

age = input("Enter your age: ")
if age < 18: # This is a logical error as we cannot compare a string with an integer.
    print("You are a minor.")
else:
    print("You are an adult.")

# Output
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-5-9b8b6b0b0e2a> in <module>
          1 age = input("Enter your age: ")
    ----> 2 if age < 18: # This is a logical error as we cannot compare a string with an integer.
          3     print("You are a minor.")
          4 else:
          5     print("You are an adult.")

    TypeError: '<' not supported between instances of 'str' and 'int'

```
### Types of Exceptions in Python

* There are several types of exceptions or logical erros in Python, these are in-built exceptions that are raised when the interpreter encounters an error.

| Exception | Description | Example |
| --- | --- | --- |
| `SyntaxError` | Raised when there is an error in Python syntax. | `print("Hello World!)` |
| `TypeError` | Raised when an operation or function is applied to an object of an inappropriate type. | `print(5 + "Hello")` |
| `AssertionError` | Raised when an assert statement fails. | `assert 2 + 2 == 5` |
| `AttributeError` | Raised when attribute assignment or reference fails. | `x = 5 y = x.append(10)` |
| `EOFError` | Raised when the input() function hits end-of-file condition. | `input("Enter your name: ")` |
| `FloatingPointError` | Raised when a floating point operation fails. | `x = 5.0 y = 0.0 z = x/y` |
| `GeneratorExit` | Raised when a generator's close() method is called. | `def mygen(): yield 1 yield 2 g = mygen() g.close()` |
| `ImportError` | Raised when the imported module is not found. | `import mymodule` |
| `IndexError` | Raised when the index of a sequence is out of range. | `x = [1, 2, 3] print(x[3])` |
| `KeyError` | Raised when a key is not found in a dictionary. | `x = {"a": 1, "b": 2} print(x["c"])` |
| `KeyboardInterrupt` | Raised when the user hits the interrupt key (Ctrl+C or Delete). | `while True: pass` |
| `MemoryError` | Raised when an operation runs out of memory. | `x = [] while True: x.append(1)` |
| `NameError` | Raised when a variable is not found in the local or global scope. | `print(x)` |
| `NotImplementedError` | Raised by abstract methods. | `class A: def myfunc(self): raise NotImplementedError` |
| `OSError` | Raised when a system operation causes a system-related error. | `f = open("myfile.txt")` |
| `OverflowError` | Raised when the result of an arithmetic operation is too large to be represented. | `x = 2 for i in range(100): x = x ** 2` |
| `ReferenceError` | Raised when a weak reference object is used to access a garbage collected referent. | `import weakref class A: pass a = A() r = weakref.ref(a) del a r() # raises ReferenceError` |
| `RuntimeError` | Raised when an error occurs that do not belong to any specific category. | `raise RuntimeError("Something went wrong")` |
| `StopIteration` | Raised when the next() method of an iterator does not point to any object. | `x = [1, 2, 3] i = iter(x) print(next(i)) print(next(i)) print(next(i)) print(next(i))` |


### Difference between Syntax Errors and Logical Errors
* Following are the differences between syntax errors and logical errors in Python:
  
| Syntax Errors | Logical Errors |
| --- | --- |
| Syntax errors occur when there is anything wrong with the syntax of the program. | Logical errors occur when the program is syntactically correct but the code results in an error. |
| Syntax errors are also known as parsing errors. | Logical errors are also known as exceptions. |
| Syntax errors can be detected by the Python interpreter. | Logical errors are detected while the program is running. |
| Syntax errors are easy to fix. | Logical errors are difficult to fix. |

## Error handling in Python

* Error handling is a process of handling errors that occur during the execution of a program.
* Error handling is an essential part of any program as it prevents the program from crashing and makes it more robust.
* There are several ways to handle errors in python, such as: `try-except`, `try-except-else`, `try-except-finally`, `try-except-else-finally`, etc.

### `try-except` block

* This is the simplest way to handle errors in Python.
* It is used to handle the exceptions or errors that occur during the execution of a program.
* The `try` block contains the code that may cause an error.
* The `except` block contains the code that is executed if an error occurs in the `try` block.
* The `except` block is executed only if an error occurs in the `try` block.
* The `except` block can handle multiple errors by using multiple `except` blocks.
* The `except` block can also be used without an error type to handle all types of errors.

```python
# Example 1
try:
    a = 10
    b = 0
    print(a/b)
except:
    print("An error occurred.")

# Output
    An error occurred.

# Example 2
try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Output
    Cannot divide by zero.

# Example 3
try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except:
    print("An error occurred.")

# Output
    Cannot divide by zero.
```

### `try-except-else` block

* This is another way to handle errors in Python.
* It is used to handle the exceptions or errors that occur during the execution of a program.
* The `try` block contains the code that may cause an error.
* The `except` block contains the code that is executed if an error occurs in the `try` block.
* The `except` block is executed only if an error occurs in the `try` block.
* The `else` block contains the code that is executed if no error occurs in the `try` block.
* The `else` block is executed only if no error occurs in the `try` block.

```python
# Example 1
try:
    a = 10
    b = 2
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("No error occurred.")

# Output
    5.0
    No error occurred.

# Example 2
try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("No error occurred.")

# Output
    Cannot divide by zero.
```

### `try-except-finally` block

* This is another way to handle errors in Python.
* It is used to handle the exceptions or errors that occur during the execution of a program.
* The `try` block contains the code that may cause an error.
* The `except` block contains the code that is executed if an error occurs in the `try` block.
* The `except` block is executed only if an error occurs in the `try` block.
* The `finally` block contains the code that is always executed whether an error occurs in the `try` block or not.
* The `finally` block is executed whether an error occurs in the `try` block or not.

```python
# Example 1
try:
    a = 10
    b = 2
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Finally block is executed.")

# Output
    5.0
    Finally block is executed.

# Example 2
try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Finally block is executed.")

# Output 
    Cannot divide by zero.
    Finally block is executed.
```

### `try-except-else-finally` block

* This is another way to handle errors in Python.
* It is used to handle the exceptions or errors that occur during the execution of a program.
* The `try` block contains the code that may cause an error.
* The `except` block contains the code that is executed if an error occurs in the `try` block.
* The `except` block is executed only if an error occurs in the `try` block.
* The `else` block contains the code that is executed if no error occurs in the `try` block.
* The `else` block is executed only if no error occurs in the `try` block.
* The `finally` block contains the code that is always executed whether an error occurs in the `try` block or not.
* The `finally` block is executed whether an error occurs in the `try` block or not.

```python
# Example 1
try:
    a = 10
    b = 2
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("No error occurred.")
finally:
    print("Finally block is executed.")

# Output
    5.0
    No error occurred.
    Finally block is executed.

# Example 2
try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("No error occurred.")
finally:
    print("Finally block is executed.")

# Output
    Cannot divide by zero.
    Finally block is executed.
```

### `raise` statement

* The `raise` statement is used to raise an exception or error manually.

```python
# Example 1
try:
    a = 10
    b = 0
    if b == 0:
        raise ZeroDivisionError
    else:
        print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Output
    Cannot divide by zero.

# Example 2
try:
    a = 10
    b = 0
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    else:
        print(a/b)
except ZeroDivisionError as e:
    print(e)

# Output
    Cannot divide by zero.
```

### `assert` statement

* The `assert` statement is used to check if a condition is true or not.
* If the condition is true, the program continues to execute.
* If the condition is false, the program raises an `AssertionError` exception.

```python
# Example 1
try:
    a = 10
    b = 0
    assert b != 0
    print(a/b)
except AssertionError:
    print("Cannot divide by zero.")

# Output
    Cannot divide by zero.

# Example 2
try:
    a = 10
    b = 0
    assert b != 0, "Cannot divide by zero."
    print(a/b)
except AssertionError as e:
    print(e)

# Output
    Cannot divide by zero.
```



