# Operators in Python

# Arithmetic Operators
# +, -, *, /, %, **, //
a = 100
b = 20

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b)  # Exponent
print(a // b)  # Floor Division

# Comparison Operators
# ==, !=, >, <, >=, <=
print(a == b)  # Equal
print(a != b)  # Not Equal
print(a > b)  # Greater Than
print(a < b)  # Less Than
print(a >= b)  # Greater Than or Equal
print(a <= b)  # Less Than or Equal

# Assignment Operators
# =, +=, -=, *=, /=, %=, **=, //=
a = 100
b = 20

a += b  # a = a + b
print(a)

a -= b  # a = a - b
print(a)

a *= b  # a = a * b
print(a)

a /= b  # a = a / b
print(a)

a %= b  # a = a % b
print(a)

a **= b  # a = a ** b
print(a)

a //= b  # a = a // b
print(a)

# Logical Operators
# and, or, not
a = 100
b = 20
c = 30

print(a > b and a > c)  # and
print(a > b or a > c)  # or
print(not a > b)  # not

# Identity Operators
# is, is not
a = 100
b = 20

print(a is b)
print(a is not b)

# Membership Operators
# in, not in
a = [10, 20, 30, 40, 50]

print(10 in a)
print(100 in a)
print(10 not in a)
print(100 not in a)

# Bitwise Operators
# &, |, ^, ~, <<, >>

# & - Bitwise AND
# | - Bitwise OR
# ^ - Bitwise XOR
# ~ - Bitwise NOT
# << - Bitwise Left Shift
# >> - Bitwise Right Shift

a = 10  # 1010
b = 4  # 0100

print(a & b)  # 0000
print(a | b)  # 1110
print(a ^ b)  # 1110
print(~a)  # 0101
print(a << 2)  # 101000
print(a >> 2)  # 0010

