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