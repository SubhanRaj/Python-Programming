# Operators in Python

In python there are many different types of operators. These operators are used to perform different operations on variables and values.

## Types of Operators

We can classify operators in python into 7 different types.

### 1. Arithmetic Operators

* Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication etc.
* Arithmetic operators are binary operators as they require two operands.
* The operands can be integer, float or complex number.
* The result of arithmetic operators is always a number.

| Operator | Description | Example |
| :---: | :---: | :---: |
| + | Addition: Adds two operands | x + y |
| - | Subtraction: Subtracts two operands | x - y |
| * | Multiplication: Multiplies two operands | x * y |
| / | Division (float): Divides the first operand by the second | x / y |
| // | Division (floor): Divides the first operand by the second | x // y |
| % | Modulus: Returns the remainder when first operand is divided by the second | x % y |
| ** | Power : Returns first raised to power second | x ** y |

### 2. Comparison Operators

* Comparison operators are used to compare values. It either returns True or False according to the condition.
* Comparison operators are binary operators as they require two operands.
* The operands can be integer, float or complex number.
* These operators are also known as Relational operators.
* The result of comparison operators is always a boolean value.
  
| Operator | Description | Example |
| :---: | :---: | :---: |
| > | Greater than: True if left operand is greater than the right | x > y |
| < | Less than: True if left operand is less than the right | x < y |
| == | Equal to: True if both operands are equal | x == y |
| != | Not equal to - True if operands are not equal | x != y |
| >= | Greater than or equal to: True if left operand is greater than or equal to the right | x >= y |
| <= | Less than or equal to: True if left operand is less than or equal to the right | x <= y |

### 3. Logical Operators

* Logical operators are used to combine conditional statements.
* Logical operators are binary operators as they require two operands.
* The operands can be integer, float or complex number.
* The result of logical operators is always a boolean value.

| Operator | Description | Example |
| :---: | :---: | :---: |
| and | Returns True if both statements are true | x < 5 and  x < 10 |
| or | Returns True if one of the statements is true | x < 5 or x < 4 |
| not | Reverse the result, returns False if the result is true | not(x < 5 and x < 10) |

### 4. Assignment Operators

* Assignment operators are used to assign values to variables.
* Assignment operators are binary operators as they require two operands.
* The operands can be integer, float or complex number.
* The result of assignment operators is always a number.

| Operator | Description | Example |
| :---: | :---: | :---: |
| = | Assign value of right side of expression to left side operand | x = y + z |
| += | Add AND: Add right side operand with left side operand and then assign to left operand | x += y |
| -= | Subtract AND: Subtract right operand from left operand and then assign to left operand | x -= y |
| *= | Multiply AND: Multiply right operand with left operand and then assign to left operand | x *= y |
| /= | Divide AND: Divide left operand with right operand and then assign to left operand | x /= y |
| %= | Modulus AND: Takes modulus using left and right operands and assign result to left operand | x %= y |
| //= | Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand | x //= y |
| **= | Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand | x **= y |

### 5. Bitwise Operators

* Bitwise operators are used to perform bitwise operations on integers.
* Bitwise operators are binary operators as they require two operands.
* The operands can be integer, float or complex number.
* The result of bitwise operators is always a number.

| Operator | Description | Example |
| :---: | :---: | :---: |
| & | Bitwise AND: Operator copies a bit to the result if it exists in both operands | x & y |
| \| | Bitwise OR: It copies a bit if it exists in either operand | x \| y |
| ^ | Bitwise XOR: It copies the bit if it is set in one operand but not both | x ^ y |

### 6. Membership Operators

* Membership operators are used to test if a sequence is presented in an object.
* Membership operators are binary operators as they require two operands.
* The operands can be integer, float or complex number.
* The result of membership operators is always a boolean value.

| Operator | Description | Example |
| :---: | :---: | :---: |
| in | Returns True if a sequence with the specified value is present in the object | x in y |
| not in | Returns True if a sequence with the specified value is not present in the object | x not in y |

### 7. Identity Operators

* Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
* Identity operators are binary operators as they require two operands.
* The operands can be integer, float or complex number.
* The result of identity operators is always a boolean value.

| Operator | Description | Example |
| :---: | :---: | :---: |
| is | Returns True if both variables are the same object | x is y |
| is not | Returns True if both variables are not the same object | x is not y |

## Operator Precedence



Operator precedence is a very important concept in programming. It defines the order in which different operators are executed. Operators with higher precedence are executed first.

* For example, multiplication has higher precedence than addition.

```python
>>> 2 + 3 * 4
14
```

* In the above example, first 3 is multiplied with 4 and then the result is added to 2. If we change the order of precedence by using parenthesis, we will get a different result.

```python
>>> (2 + 3) * 4
20
```

* In the above example, first 2 is added to 3 and then the result is multiplied with 4.
* Following List shows the operator precedence in Python (from highest precedence to lowest precedence).
* Operators in the same box have the same precedence.

|Sr. No.| Operator | Description | Precedence |
| :---: | :---: | :---: | :---: |
| 1 | ** | Exponent | Highest |
| 2 | *, /, //, % | Multiplication, Division, Floor Division, Modulus | 2nd Highest |
| 3 | +, - | Addition, Subtraction | 3rd Highest |
| 4 | <, <=, >, >= | Comparison Operators | 4th Highest |
| 5 | ==, != | Equality Operators | 5th Highest |
| 6 | =, +=, -=, *=, /=, //=, %=, **= | Assignment Operators | Lowest |



