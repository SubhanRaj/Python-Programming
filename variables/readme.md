 # Variables in Python

 ## What is A Variable?
* In python, variables are containers for storing data values.
* Unlike other programming languages, Python has no command for declaring a variable.
* A variable is created the moment you first assign a value to it.
* Following are some examples of variables.

```python
a = 30
b = 20
c = 10
name = "Python"
release_year = "1991"
```

## Rules for Naming Variables in Python
Following are the rules for naming Variables in Python
1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. Variable names are case-sensitive (age, Age and AGE are three different variables)

## Types of Variables in Python
Following are the types of variables in Python

1. **Numbers** : Integers, Floats, Complex Numbers
2. **String** : A string is a sequence of characters.
3. **List**: A list is a collection which is ordered and changeable. Allows duplicate members.
4. **Tuple**: A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
5. **Dictionary** : A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
6. **Boolean** : A Boolean value is either true or false.

### Numbers:
In Python, there are three numeric types.
1. **Integers** : Integers are whole numbers, positive or negative, without decimals, of unlimited length.
2. **Floats** : Floats are real numbers, with a decimal point dividing the integer and fractional parts.
3. **Complex Numbers** : Complex numbers are written with a "j" as the imaginary part.

```python
a = 10 # Integer
b = 20.5 # Float
c = 1+3j # Complex Number
```
### Strings:
In python strings are surrounded by either single quotation marks, or double quotation marks.
```python
name = "Python"
```

### Lists:
In python lists represents a collection of items. Lists are ordered, changeable and allow duplicate values.
* **Syntax of List** : list = [item1, item2, item3, ...]
* List items are ordered, changeable, and allow duplicate values.
* List uses () brackets.
```python
list = [1, 2, 3, 4, 5]
```

### Tuples:
In python tuples represents a collection of items. Tuples are ordered, unchangeable and allow duplicate values.
* **Syntax of Tuple** : tuple = (item1, item2, item3, ...)
* Tuple items are ordered, unchangeable, and allow duplicate values.
* Tuple uses [] brackets.
```python
tuple = (1, 2, 3, 4, 5)
```
### Dictionary:
In python dictionary represents a collection of items. Dictionaries are unordered, changeable and indexed. No duplicate values are allowed.
* **Syntax of Dictionary** : dict = {key1: value1, key2: value2, key3: value3, ...}
* Dictionary items are unordered, changeable, and does not allow duplicate values.
* Dictionary uses {} brackets.
```python
dict = {'name': 'Python', 'age': 30}
```

### Boolean:
In python Boolean represents a collection of items. Boolean values are either true or false.
* **Syntax of Boolean** : bool = True or False
* Boolean values are either true or false.
* Boolean Variables uses True or False keywords, both are case sensitive.
```python
bool = True
```


## Mutable and Immutable Variables
In Python, variables can be mutable or immutable. 
* Mutable variables can be changed after it has been created.
* Immutable variables cannot be changed after it has been created.
* Following are the examples of mutable and immutable variables.

```python
# Mutable Variables
list = [1, 2, 3, 4, 5]
dict = {'name': 'Python', 'age': 30}

# Immutable Variables
tuple = (1, 2, 3, 4, 5)
string = "Python"
```
