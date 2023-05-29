# List in Python

* In Python programming, a list is created by placing all the items (elements) inside a square bracket [ ], separated by commas.
* List is an inbuilt data structure in Python. It is a collection of elements which is ordered and changeable.
* Lists are used to store multiple items in a single variable.
* List is a mutable data type, i.e., the value of a list can be altered.
* Lists are similar to arrays in C language.
* Lists are used to store multiple items in a single variable.

## Creating a List

* We can create a list by placing a comma-separated sequence of items in square brackets [] as per given syntax:

```python
list_name = [item1, item2, item3, ...]
```

* Lists can contain items of different data types, but usually, the items all have the same data type.

```python
# Example
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
```

* A list can also contain a list within a list. Such type of list is called a nested list.

```python
# Example
list1 = ["apple", "banana", "cherry", [1, 5, 7, 9, 3]]
```

## Accessing Items in a List

* We can access individual items in a list by using an index in square brackets.

```python
# Example
list1 = ["apple", "banana", "cherry"]
print(list1[0]) # Output: apple
print(list1[1]) # Output: banana
print(list1[2]) # Output: cherry
```
* We can also use negative indexing to access items in a list. Negative indexing starts from the end of the list.

```python
# Example
list1 = ["apple", "banana", "cherry"]
print(list1[-1]) # Output: cherry
print(list1[-2]) # Output: banana
print(list1[-3]) # Output: apple
```

## List Operations

* We can perform various operations on a list, some of which are as follows:
  
  ### 1. List Concatenation

    * We can concatenate two or more lists using the + operator. This is also called concatenation.
    
    ```python
    # Example
    list1 = ["apple", "banana", "cherry"]
    list2 = [1, 5, 7, 9, 3]
    list3 = list1 + list2
    print(list3) # Output: ['apple', 'banana', 'cherry', 1, 5, 7, 9, 3]
    ```

    ### 2. List Repetition

    * We can repeat a list a given number of times using the * operator.
    
    ```python
    # Example
    list1 = ["apple", "banana", "cherry"]
    list2 = list1 * 2
    print(list2) # Output: ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']
    ```

    ### 3. List Slicing

    * We can access a range of items in a list by using the slicing operator :.
    * `:` is called the slicing operator.
    * The index before `:` is the starting index of the slice and the index after `:` is the ending index of the slice.
    * The starting index is inclusive and the ending index is exclusive.
    * If we don't specify the starting index, the slice will start from the beginning of the list.
    * If we don't specify the ending index, the slice will go to the end of the list.
    * We can also use negative indexing in slicing.
    * If we use negative indexing, the slice will start from the end of the list.
    * If we use negative indexing, the slice will go to the beginning of the list.
  
    
    ```python
    # Example
    list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(list1[2:5]) # Output: ['cherry', 'orange', 'kiwi']
    print(list1[:4]) # Output: ['apple', 'banana', 'cherry', 'orange']
    print(list1[2:]) # Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']
    print(list1[-4:-1]) # Output: ['orange', 'kiwi', 'melon']
    ```

    ### 4. List Length

    * We can find the length of a list using the `len()` function.
    
    ```python
    # Example
    list1 = ["apple", "banana", "cherry"]
    print(len(list1)) # Output: 3
    ```

    ### 5. List Membership

    * We can check if an item is present in a list or not using the `in` and `not in` operators i.e. the **membership operators**.
    * The `in` operator returns `True` if the item is present in the list, otherwise it returns `False`.
    
    ```python
    # Example
    list1 = ["apple", "banana", "cherry"]
    print("banana" in list1) # Output: True
    print("orange" in list1) # Output: False
    ```

    * The `not in` operator returns `True` if the item is not present in the list, otherwise it returns `False`.
    
    ```python
    # Example
    list1 = ["apple", "banana", "cherry"]
    print("banana" not in list1) # Output: False
    print("orange" not in list1) # Output: True
    ```

## List Methods

* We can perform various operations on a list using its methods, some of which are as follows:

  ### 1. `append()`

  * We can add an item to the end of a list using the `append()` method.
  
  ```python
  # Example
  list1 = ["apple", "banana", "cherry"]
  list1.append("orange")
  print(list1) # Output: ['apple', 'banana', 'cherry', 'orange']
  ```

  ### 2. `insert()`

  * We can insert an item at a given index in a list using the `insert()` method.
  
  ```python
  # Example
  list1 = ["apple", "banana", "cherry"]
  list1.insert(1, "orange")
  print(list1) # Output: ['apple', 'orange', 'banana', 'cherry']
  ```

  ### 3. `remove()`

  * We can remove an item from a list using the `remove()` method.
  * The `remove()` method removes the first occurrence of the item from the list.
  
  ```python
  # Example
  list1 = ["apple", "banana", "cherry"]
  list1.remove("banana")
  print(list1) # Output: ['apple', 'cherry']
  ```

  ### 4. `pop()`

  * We can remove an item from a list using the `pop()` method.
  * The `pop()` method removes the item at the given index from the list.
  * If we don't specify the index, the `pop()` method removes the last item from the list.
  
  ```python
  # Example
  list1 = ["apple", "banana", "cherry"]
  list1.pop()
  print(list1) # Output: ['apple', 'banana']
  list1.pop(0)
  print(list1) # Output: ['banana']
  ```

  ### 5. `clear()`

  * We can remove all the items from a list using the `clear()` method.
  
  ```python
  # Example
  list1 = ["apple", "banana", "cherry"]
  list1.clear()
  print(list1) # Output: []
  ```

  ### 6. `index()`

  * We can find the index of an item in a list using the `index()` method.
  * The
  * The `index()` method returns the index of the first occurrence of the item in the list.
  
  ```python
    # Example
    list1 = ["apple", "banana", "cherry"]
    print(list1.index("banana")) # Output: 1
    ```

    ### 7. `count()`

    * We can count the number of times an item occurs in a list using the `count()` method.
    
    ```python
    # Example
    list1 = ["apple", "banana", "cherry", "banana", "banana"]
    print(list1.count("banana")) # Output: 3
    ```

    ### 8. `sort()`

    * We can sort the items of a list using the `sort()` method.
    * The `sort()` method sorts the items of the list in ascending order by default.
    
    ```python
    # Example
    list1 = ["apple", "banana", "cherry"]
    list1.sort()
    print(list1) # Output: ['apple', 'banana', 'cherry']
    ```

    * We can also sort the items of a list in descending order using the `sort()` method.
    * We can do this by passing the `reverse=True` argument to the `sort()` method.
    
    ```python
    # Example
    list1 = ["apple", "banana", "cherry"]
    list1.sort(reverse=True)
    print(list1) # Output: ['cherry', 'banana', 'apple']
    ```

    ### 9. `reverse()`
    
    * We can reverse the items of a list using the `reverse()` method.
    
    ```python
    # Example
    list1 = ["apple", "banana", "cherry"]
    list1.reverse()
    print(list1) # Output: ['cherry', 'banana', 'apple']
    ```

    ### 10. `copy()`

    * We can copy a list using the `copy()` method.
    
    ```python
    # Example
    list1 = ["apple", "banana", "cherry"]
    list2 = list1.copy()
    print(list2) # Output: ['apple', 'banana', 'cherry']
    ```

## List Comprehension

* List comprehension is a concise way of creating lists.
* It is a way of creating a new list from an existing list.
* It is a one-line shorthand for creating a new list.
* It is a more readable and faster way of creating lists.
* It is a combination of a `for` loop and a `list` object.
* It is a way of applying a function to a list.
* It is a way of filtering a list.
* Syntax

```python
new_list = [expression for item in list]
```

* Example

```python
# Example
list1 = [1, 2, 3, 4, 5]
list2 = [i * 2 for i in list1]
print(list2) # Output: [2, 4, 6, 8, 10]
```






