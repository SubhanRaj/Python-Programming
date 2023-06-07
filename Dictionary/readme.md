# Python Dictionary

* In python dictionary is an useful data structure which is used to store data in key-value pairs.
* Dictionary is also called associative array.
* Disctinary is a mutable data structure.
* Dictionary is unordered.
* Dictionary is represented by curly braces `{}`.
* Dictionary is also called `dict`.
## Operations on Dictionary
* There are a number of operations that can be performed on dictionary.
* This include creating a dictionary, accessing elements of a dictionary, adding elements to a dictionary, updating elements of a dictionary, deleting elements of a dictionary, deleting a dictionary.

### Creating a dictionary

* We can create a dictionary using the following syntax:

```python
dictionary_name = {key1: value1, key2: value2, key3: value3}
```

* Also using following syntax:

```python
dictionary_name = {
    key1: value1,
    key2: value2,
    key3: value3
}
```

* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech"
}
```

### Accessing elements of a dictionary

* We can access elements of a dictionary using the following syntax:

```python
dictionary_name[key]
```

* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech"
}
print(student["name"])
print(student["age"])
print(student["course"])
```

* Also we can use `range()` along with `for` loop to access elements of a dictionary.
* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech"
}
for key in student:
    print(key, student[key])
```

### Adding elements to a dictionary

* We can add elements to a dictionary using the following syntax:

```python
dictionary_name[key] = value
```

* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech"
}
student["roll_no"] = 1
print(student)
```

### Updating elements of a dictionary
* We can update elements of a dictionary using the following syntax:

```python
dictionary_name[key] = new_value
```

* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech"
}
student["age"] = 21
print(student)
```

### Deleting elements of a dictionary

* We can delete elements of a dictionary using the following syntax:

```python
del dictionary_name[key]
```

* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech"
}
del student["age"]
print(student)
```

### Deleting a dictionary

* We can delete a dictionary using the following syntax:

```python
del dictionary_name
```

* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech"
}
del student
print(student)
```

* This will give an error as `student` is deleted.


## Dictionary Methods

* There are a number of methods that can be used on dictionary.
* These methods are used to perform additional operations on dictionary.
* It includes `clear()`, `copy()`, `fromkeys()`, `get()`, `items()`, `keys()`, `pop()`, `popitem()`, `setdefault()`, `update()`, `values()` etc.
* Let's see some of these methods.


### clear()

* We can use `clear()` method to remove all elements from a dictionary.
* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech"
}

student.clear()
print(student)
```

### copy()

* We can use `copy()` method to copy a dictionary.
* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech"
}

student_copy = student.copy()
print(student_copy)
```

### fromkeys()

* We can use `fromkeys()` method to create a dictionary from a sequence of keys.
* Example:

```python
keys = ("name", "age", "course")
student = dict.fromkeys(keys)
print(student)
```

* We can also specify a value for all keys.
* Example:

```python
keys = ("name", "age", "course")
student = dict.fromkeys(keys, "John")
print(student)
```

### get()

* We can use `get()` method to get the value of a key.
* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech"
}

print(student.get("name"))
```

* If the key is not present in the dictionary then it will return `None`.
* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech"
}

print(student.get("roll_no"))
```

* We can also specify a default value to return if the key is not present in the dictionary.
* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech"
}

print(student.get("roll_no", 1))
```

### items()

* We can use `items()` method to get a list of key-value pairs.
* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech"
}

print(student.items())
```

### keys()

* We can use `keys()` method to get a list of keys.
* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech"
}

print(student.keys())
```

### pop()

* We can use `pop()` method to remove an element from a dictionary.
* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech",
    "roll_no": 1
}

student.pop("roll_no")
print(student)
```

* We can also specify a default value to return if the key is not present in the dictionary.
* Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "B.Tech",
    "roll_no": 1
}

student.pop("roll_no", 1)
print(student)
```




