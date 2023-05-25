# Strings in Python

In Python Strings are sequences of characters, using the syntax of either single quotes or double quotes:

```python
# Single word
'hello'

# Entire phrase
'This is also a string'

# We can also use double quote
"String built with double quotes"

```
## String Operations in Python
### Declaring a string

We can simply declare a string by assigning a value to a variable. For example:

```python
# Assign s as a string
s = 'Hello World'
```

### Printing a string

We can print a string using `print()` function. For example:

```python
# Print the string
print(s)
```
    Hello World

### String Indexing

We can use `[]` operator to access an index of a string. For example:

```python
# Show first element (in this case a letter)
print(s[0])
```
    H

### String Slicing

We can use `[:]` operator to slice a string. For example:

```python
# Show first element (in this case a letter)
print(s[1:])
```
    ello World

## Various String Methods

### Upper Case

We can use `upper()` method to convert a string to upper case. For example:

```python
# Upper Case a string
print(s.upper())
```
    HELLO WORLD

### Lower Case

We can use `lower()` method to convert a string to lower case. For example:

```python
# Lower Case a string
print(s.lower())
```
    hello world

### Split

We can use `split()` method to split a string. For example:

```python
# Split a string by blank space (this is the default)
print(s.split())
```
    ['Hello', 'World']


### Split by a specific element (doesn't include the element that was split on)

We can use `split()` method to split a string by a specific element. For example:

```python
# Split by a specific element (doesn't include the element that was split on)
print(s.split('W'))
```
    ['Hello ', 'orld']
    
### Formatting

We can use `format()` method to add formatted objects to a string. For example:

```python
# Formatting
print('Insert another string with curly brackets: {}'.format('The inserted string'))
```
    Insert another string with curly brackets: The inserted string

### Finding

We can use `find()` method to find the first occurrence of a substring. For example:

```python
# Location and Counting
print(s.count('o'))
```
    2

### Replacing

We can use `replace()` method to replace a substring with another string. For example:

```python
# Replacing
print(s.replace('World','Universe'))
```
    Hello Universe
    
    





