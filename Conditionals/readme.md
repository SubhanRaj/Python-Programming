# Conditionals in Python

## What are Conditionals?

* Conditionals are used to execute a piece of code only if a certain condition is satisfied.
* In python, we use the `if`, `elif` and `else` keywords to create conditionals.

## Syntax of Conditionals

```python
if condition:
    # code to be executed if condition is True
elif condition:
    # code to be executed if condition is True
else:
    # code to be executed if all conditions are False
```

### if

* The `if` keyword is used to create a conditional.
* The code inside the `if` block is executed only if the condition is True.
* The `if` block is always followed by a condition.
* The `if` block can be followed by an optional `elif` block and an optional `else` block.
* The `if` block can be followed by any number of `elif` blocks.
* The `if` block can be followed by at most one `else` block.
* The `if` block is always followed by a colon (`:`).
* The `if` block is always followed by an indented block of code.
* The `if` block can be followed by an optional `elif` block.
* **Syntax**
```python
if condition:
    # code to be executed if condition is True
```
* **Example**
```python
if 5 > 2:
    print("5 is greater than 2")
```

### elif

* The `elif` keyword is used to create a conditional.
* The code inside the `elif` block is executed only if the condition is True.
* The `elif` block is always preceded by an `if` block.
* The `elif` block is always followed by a condition.
* The `elif` block is always followed by a colon (`:`).
* The `elif` block is always followed by an indented block of code.
* The `elif` block can be followed by an optional `elif` block.
* The `elif` block can be followed by an optional `else` block.
* **Syntax**
```python
if condition:
    # code to be executed if condition is True
elif condition:
    # code to be executed if condition is True
```
* **Example**
```python
if 5 > 2:
    print("5 is greater than 2")
elif 5 < 2:
    print("5 is less than 2")
```

### else

* The `else` keyword is used to create a conditional.
* The code inside the `else` block is executed only if all the conditions are False.
* The `else` block is always preceded by an `if` block.
* The `else` block is always followed by a colon (`:`).
* The `else` block is always followed by an indented block of code.
* The `else` block can be followed by an optional `elif` block.
* The `else` block can be followed by an optional `else` block.
* **Syntax**
```python
if condition:
    # code to be executed if condition is True
else:
    # code to be executed if all conditions are False
``` 
* **Example**
```python
if 5 > 2:
    print("5 is greater than 2")
else:
    print("5 is not greater than 2")
```

## Nested Conditionals

* In Python, we can create nested conditionals. In nested conditionals, we can have an `if` block inside another `if` block, an `elif` block inside another `elif` block and an `else` block inside another `else` block.
* **Syntax**
```python
if condition:
    # code to be executed if condition is True
    if condition:
        # code to be executed if condition is True
    elif condition:
        # code to be executed if condition is True
    else:
        # code to be executed if all conditions are False
elif condition:
    # code to be executed if condition is True
    if condition:
        # code to be executed if condition is True
    elif condition:
        # code to be executed if condition is True
    else:
        # code to be executed if all conditions are False
else:
    # code to be executed if all conditions are False
    if condition:
        # code to be executed if condition is True
    elif condition:
        # code to be executed if condition is True
    else:
        # code to be executed if all conditions are False
```
* **Example**
```python
if 5 > 2:
    print("5 is greater than 2")
    if 5 > 2:
        print("5 is greater than 2")
    elif 5 < 2:
        print("5 is less than 2")
    else:
        print("5 is not greater than 2")
elif 5 < 2:
    print("5 is less than 2")
    if 5 > 2:
        print("5 is greater than 2")
    elif 5 < 2:
        print("5 is less than 2")
    else:
        print("5 is not greater than 2")
else:
    print("5 is not greater than 2")
    if 5 > 2:
        print("5 is greater than 2")
    elif 5 < 2:
        print("5 is less than 2")
    else:
        print("5 is not greater than 2")
```

## Short Hand Conditionals

* In Python, we can create short hand conditionals. In short hand conditionals, we can have an `if` block without an `else` block.
* **Syntax**
```python
if condition: # code to be executed if condition is True
```
* **Example**
```python
if 5 > 2: print("5 is greater than 2")
```



