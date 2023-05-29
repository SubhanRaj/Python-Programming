# Range in Python

In Python, the `range()` function is used to generate a sequence of numbers. The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
## key Points to remember

* `range()` is used to generate a sequence of numbers.
* `range()` is a built-in function in Python.
* `range()` returns a sequence of numbers.
* `range()` takes three parameters.
  * `start` - the starting number of the sequence.
  * `stop` - the number to stop before.
  * `step` - the increment value.
  * In this the `stop` parameter is required and the other two i.e. `start` and `step` are optional.
  * `start` defaults to 0.
  * `step` defaults to 1.
  * `range()` returns a sequence of numbers from `start` to `stop - 1`.

## Syntax of range()

```python
range(stop) # this will generate a sequence of numbers from 0 to stop - 1
range(start, stop) # this will generate a sequence of numbers from start to stop - 1
range(start, stop, step) # this will generate a sequence of numbers from start to stop - 1, incrementing by step
```

## Usages Examples of range()

```python
range(5) # this will generate a sequence of numbers from 0 to 4
range(1, 5) # this will generate a sequence of numbers from 1 to 4
range(1, 5, 2) # this will generate a sequence of numbers from 1 to 4, incrementing by 2
```

## range() with for loop

* We use the `range()` function in for loops to iterate through a sequence of numbers.

```python
for i in range(5):
    print(i)
```

## range() with list()

* We can use the `range()` function to generate a list of numbers.

```python
list(range(5)) # this will generate a list of numbers from 0 to 4
list(range(1, 5)) # this will generate a list of numbers from 1 to 4
list(range(1, 5, 2)) # this will generate a list of numbers from 1 to 4, incrementing by 2
```

## range() with tuple()

* We can use the `range()` function to generate a tuple of numbers.

```python
tuple(range(5)) # this will generate a tuple of numbers from 0 to 4
tuple(range(1, 5)) # this will generate a tuple of numbers from 1 to 4
tuple(range(1, 5, 2)) # this will generate a tuple of numbers from 1 to 4, incrementing by 2
```

## range() with set()

* We can use the `range()` function to generate a set of numbers.

```python
set(range(5)) # this will generate a set of numbers from 0 to 4
set(range(1, 5)) # this will generate a set of numbers from 1 to 4
set(range(1, 5, 2)) # this will generate a set of numbers from 1 to 4, incrementing by 2
```





