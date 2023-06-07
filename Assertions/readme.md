# Assertions in Python

* In Python, assertions are statements that assert or state a fact confidently in your program. For example, while writing a division function, you're confident the divisor shouldn't be zero, you assert divisor is not equal to zero.
* Assertions are simply boolean expressions that checks if the conditions return true or not. If it is true, the program does nothing and move to the next line of code. However, if it's false, the program stops and throws an error.
* Assertions can be made using the `assert` keyword.
* Syntax:
```python
assert condition, error_message
```
* Example:
```python
def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Enter a number: ")
    assert num.isnumeric(), "Please enter a number"
    print(divisors(int(num)))
    print("Program finished")

if __name__ == '__main__':
    run()
```

* In the example above, we're using the `assert` keyword to check if the input is a number. If the input is not a number, the program will stop and throw an error.
* The `assert` keyword takes in two arguments:
    * A condition to check for.
    * An error message to display when the condition is false.
* If the condition is true, the program does nothing and move to the next line of code.
* If the condition is false, the program stops and throws an error with the error message.
* In the example above, if the input is not a number, the program will stop and throw an error with the message "Please enter a number".
* If the input is a number, the program will continue to the next line of code.
* The `assert` keyword is useful when debugging code. It allows you to easily find errors in your code.
* The `assert` keyword is used to test if a condition in your code returns true, if not, the program will raise an AssertionError.
* The `assert` keyword is followed by a condition.

## Using Assertions in Traffic Light Simulation

* In a traffic light simulation, assertions can be used to validate the correctness of the traffic light states and ensure that the simulation follows the expected behavior. Here's an example of how assertions can be used in a traffic light simulation:
* Example:
```python
def simulate_traffic_light(color):
    assert color in ['red', 'yellow', 'green'], "Invalid traffic light color"  # Assertion to validate color

    if color == 'red':
        print("Stop!")
    elif color == 'yellow':
        print("Prepare to stop!")
    elif color == 'green':
        print("Go!")

# Testing the traffic light simulation
simulate_traffic_light('red')  # Valid color, output: Stop!
simulate_traffic_light('yellow')  # Valid color, output: Prepare to stop!
simulate_traffic_light('green')  # Valid color, output: Go!

simulate_traffic_light('blue')  # Invalid color, raises AssertionError
```
* In the above code, the simulate_traffic_light() function accepts a color as input and uses assertions to ensure that the color is one of the expected values: 'red', 'yellow', or 'green'. If the color is not one of these values, an AssertionError is raised, indicating that the input is invalid.