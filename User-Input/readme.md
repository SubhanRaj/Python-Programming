# User Input in Python

In Python, we can use the `input()` function to take input from the user. The `input()` function reads the data from the keyboard and returns it as a string.

## Syntax of input() function

```python
variable = input("Enter your name: ")
```

## Key points to remember
* The `input()` function takes one argument that is used as a prompt.
* The `input()` function always returns a string.
* If you want to take input as an integer, you need to typecast it using `int()` function.

## Example of input() function

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello " + name + "!")
print("You are " + str(age) + " years old.")
```

## Concatination

In Python, we can use the `+` operator to concatenate two strings. The `+` operator concatenates the second string to the first string.

```python
# Concatenation of two strings
str1 = "Hello"
str2 = "World"
str3 = str1 + str2
print(str3)
```

    HelloWorld

## Type Conversion

Python by-default takes the input as a string, we have various different methods to convert the string into other data types.

## Convert string to integer
* We can use `int()` function to convert a string to an integer.

```python
# Convert string to integer
str1 = "10"
num1 = int(str1)
print(num1)
```

    10

## Convert string to float
* We can use `float()` function to convert a string to a float.

```python
# Convert string to float
str1 = "10.5"
num1 = float(str1)
print(num1)
```

    10.5

## Convert string to boolean
* We can use `bool()` function to convert a string to a boolean.

```python
# Convert string to boolean
str1 = "True"
bool1 = bool(str1)
print(bool1)
```

    True

## Convert string to list
* We can use `list()` function to convert a string to a list.

```python
# Convert string to list
str1 = "Hello"
list1 = list(str1)
print(list1)
```

    ['H', 'e', 'l', 'l', 'o']

## Convert string to tuple
* We can use `tuple()` function to convert a string to a tuple.

```python
# Convert string to tuple
str1 = "Hello"
tuple1 = tuple(str1)
print(tuple1)
```

    ('H', 'e', 'l', 'l', 'o')

## Convert string to set
* We can use `set()` function to convert a string to a set.

```python
# Convert string to set
str1 = "Hello"
set1 = set(str1)
print(set1)
```

    {'e', 'l', 'H', 'o'}

## Convert string to dictionary
* We can use `eval()` function to convert a string to a dictionary.

```python
# Convert string to dictionary
str1 = "{'name': 'John', 'age': 30}"
dict1 = eval(str1)
print(dict1)
```

    {'name': 'John', 'age': 30}

## Convert string to complex
* We can use `complex()` function to convert a string to a complex number.

```python
# Convert string to complex
str1 = "10+5j"
complex1 = complex(str1)
print(complex1)
```

    (10+5j)

## Convert string to bytes
* We can use `bytes()` function to convert a string to a bytes object.

```python
# Convert string to bytes
str1 = "Hello"
bytes1 = bytes(str1, 'utf-8')
print(bytes1)
```

    b'Hello'

