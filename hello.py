# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 21:47:15 2023

@author: upmanyu
"""
import sys
print("hello world!")  # this will print the code in one line only

print("""
    my
    ________first
    ____________________code""")  # this will print the code as it is written in the editor

# print('\033[H\033[J') #for clearing the screen   ... but not
# %%
print("Enter First Number")
a = int(input())  # changing the data type at runtime is called typecasting

print("Enter Second Number")
b = int(input())

c = a+b

print("sum=", c)
# %%
print("Enter First input")
a = input()

print("Enter Second input")
b = input()

c = a + b  # concatenation
# if any operator in a particular code performs different
# task then its know as operator overloading

print("Answer=", c)
# %%
print("Enter your name\n")
s = input()

print("Enter your amount\n")
b = float(input())
print("your name is %s and the amount you have spent is %f" % (s, b))
# %s is a format specifier to inform the compiler about the type of data that system, planes to use.
# %%
print("Enter your name\n")
s = input()

print("Enter your amount\n")
b = float(input())
print("your name is %s and the amount you have spent is %0.2f" % (s, b))
# %%
# %%
print("Enter your name\n")
s = input()

print("Enter your amount\n")
b = float(input())
print("your name is %s and the amount you have spent is %0.5f" % (s, b))
# %%
print("Enter your name\n")
s = input()
print("Enter your amount\n")
b = float(input())
print("your name is {0} and the amount you have spent is {1}".format(s, b))
# %%
print("ENTER TWO DIGITS NUMBER")
a = int(input())
print("{:05d}" .format(a))  # leading zeros
# %%
print("{:05d}" .format(int(input())))  # leading zeros
# %%
print("Enter First Number")
a = int(input())

print("Enter Second Number")
b = int(input())
# basic set of operator
# c = a+b
# c = a-b
# c = a%b #mod operator returns remended
# c = a/b #div operator
# c = a*b
# c = a**b  # square
c = a//b  # quotient
print("Result=", c)
# %%
# membership operators in python ('in' and 'not in') =
# basically sees whether given value is present in a
# given set of values and then it returns true or false
s = "I LOVE PYTHON"
ans = "HATE" in s
print("RESULT = ", ans)
# %%
s = "I LOVE PYTHON"
ans = "Love" in s
print("RESULT = ", ans)
# %%
s = "I LOVE PYTHON"
ans = "Love" not in s
print("RESULT = ", ans)
# %%
s = "I LOVE PYTHON"
print("Love" not in s)
# %%
# slicing methods
print("HEY")
print("HEY" * 5)
# %%
# string and slicing operations on string
s = "AN APPLE A DAY KEEPS DOCTOR AWAY"
print(s)
print(s[3])
print(s[3:8])
print(s[4:])
print(s[:7])
# %%
# list - sequence of data i.e data can be of different data type
list1 = ['English', 'Maths', 'physics', 'chemistry', 1000, 2000, 234.76]
print(list1)
print("Value available at index 2: ")
print(list1[2])
list1[2] = 'History'
print("New value available at index 2: ")
print(list1[2])
print(list1[2:6])
list2 = ['Algebra', 'Geography', 'Hindi', 145.73]
list3 = list1 + list2  # concatination
print(list3)
# %%
list1 = ['English', 'Maths', 'physics', 'chemistry', 1000, 2000, 234.76]
print(list1)
a = list1.count('Maths')
print("count= ", a)
list1.pop()
print(list1)
del list1[2]
print(list1)
list1.append('Apple')
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)
# %%
list1 = [1000, 6, 77, 9999, 542, 2000, 234]
list1.sort()
print(list1)
# %%
tup1 = ('English', 'Maths', 'physics', 'chemistry', 1000, 2000, 234.76)
print(tup1)
print("value available at index 2: ")
print(tup1[2])
print(tup1[2:6])
tup2 = ('Algebra', 'Geography', 'Hindi', 145.73)
tup3 = tup1 + tup2  # concatination
print(tup3)
# %%
my_data = (11, 22, 33, 44, 55, 66, 77, 88, 99)
print(my_data)
print(my_data[2:5])
print(my_data[:4])
print(my_data[4:])
print(my_data[4:-1])
print(my_data[4:0])  # returns ()
print(my_data[4:-2])
print(my_data[4:-4])  # return (55,)
print(my_data[4:-6])  # return ()
print(my_data[4:-5])  # return ()
print(my_data[:])
print(len(my_data))
print(my_data[4:-1])
c = len(my_data)
print(my_data[4:c])
print(my_data[4:9])
# %%
d = {"1": "Dhawan", "2": "Rohit", "3": "Virat", "4": "Dhoni", "5": "Rayudu",
     "6": "Hardik", "7": "Bhuvi", "8": "Shami", "9": "Bumrah", "10": "Jadeja", "11": "Umesh"}
print(d)
print(d['3'], d['5'], d['7'])
# %%
Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
Boys = {'Tim': 18, 'Charlie': 12, 'Robert': 25}
Girls = {'Tiffany': 22}
studentX = Boys.copy()
studentY = Girls.copy()
print(studentX)
print(studentY)
Girls.update({"Anna": 43})
print(Girls)
a = list(Dict.keys())
print(a)
a.sort()
print(a)
del Dict['Charlie']
print(Dict)
print("Students Name: %s" % Dict.items())
# %%
# =============================================================================
# write a python program to read a number and convert it to its hexadecimal
# and octadecimal equivalent from scratch
# =============================================================================


def decimal_to_hexadecimal(decimal_num):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""

    if decimal_num == 0:
        return "0"

    while decimal_num > 0:
        remainder = decimal_num % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        decimal_num //= 16

    return hexadecimal


def decimal_to_octal(decimal_num):
    octal = ""

    if decimal_num == 0:
        return "0"

    while decimal_num > 0:
        remainder = decimal_num % 8
        octal = str(remainder) + octal
        decimal_num //= 8

    return octal


if __name__ == "__main__":
    try:
        decimal_input = int(input("Enter a decimal number: "))
        if decimal_input < 0:
            raise ValueError("Please enter a non-negative integer.")

        hexadecimal_result = decimal_to_hexadecimal(decimal_input)
        octal_result = decimal_to_octal(decimal_input)

        print(f"Hexadecimal: {hexadecimal_result}")
        print(f"Octal: {octal_result}")

    except ValueError as e:
        print(f"Error: {e}")

# =============================================================================
# OR
# =============================================================================


def decimal_to_base(decimal_num, base):
    hex_chars = "0123456789ABCDEF"
    result = ""

    if decimal_num == 0:
        return "0"

    while decimal_num > 0:
        remainder = decimal_num % base
        result = hex_chars[remainder] + result
        decimal_num = decimal_num // base

    return result


if __name__ == "__main__":
    try:
        decimal_input = int(input("Enter a decimal number: "))
        if decimal_input < 0:
            raise ValueError("Please enter a non-negative integer.")

        hexadecimal_result = decimal_to_base(decimal_input, 16)
        octal_result = decimal_to_base(decimal_input, 8)

        print(f"Hexadecimal: {hexadecimal_result}")
        print(f"Octal: {octal_result}")

    except ValueError as e:
        print(f"Error: {e}")

# =============================================================================
# OR use hex and oct inbuilt function
# =============================================================================
n = int(input("ENTER THE NUMBER= "))
print("Hexadecimal Equivalent= ", str(hex(n))[2:].upper())
print("Octadecimal Equivalent= ", str(oct(n))[2:].upper())

# %%
# =============================================================================
# The `f` before `print` is used to create an f-string, also known as a formatted
# string literal. It allows us to embed expressions inside curly braces `{}` within the string.
# These expressions are evaluated and replaced with their corresponding values
# in the final string.
#
# In the context of the program, using f-strings allows us to easily include the
# converted hexadecimal and octal numbers in the output string without the need for
# additional string concatenation or conversion functions. This makes the code more
# concise and readable.
#
# Here's an example of how f-strings work:
# =============================================================================

name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old."
print(message)

# =============================================================================
# Output:
# =============================================================================
# =============================================================================
# ```
# My name is Alice and I am 30 years old.
# ```
# =============================================================================
# https://www.cuemath.com/numbers/decimal-to-octal/


def decimal_to_base(decimal_num, base):
    hex_chars = "0123456789ABCDEF"
    result = ""

    if decimal_num == 0:
        return "0"

    integer_part = int(decimal_num)
    fractional_part = decimal_num - integer_part

    while integer_part > 0:
        remainder = integer_part % base
        result = hex_chars[remainder] + result
        integer_part = integer_part // base

    result += "."

    # Handle the fractional part (up to 12 decimal places)
    for _ in range(12):
        fractional_part *= base
        digit = int(fractional_part)
        result += hex_chars[digit]
        fractional_part -= digit

    return result


if __name__ == "__main__":
    try:
        decimal_input = float(input("Enter a decimal number: "))

        hexadecimal_result = decimal_to_base(decimal_input, 16)
        octal_result = decimal_to_base(decimal_input, 8)
        binary_result = decimal_to_base(decimal_input, 2)

        print(f"Hexadecimal: {hexadecimal_result}")
        print(f"Octal: {octal_result}")
        print(f"Binary: {binary_result}")

    except ValueError as e:
        print(f"Error: {e}")

# %%

# =============================================================================
# write a program to calculate the area of a circle
# =============================================================================
r = float(input("Enter the radius of the circle: "))
Area = 3.14 * r**2
print(f"Area for the circle with radius {r}= {Area}")

# %%

# =============================================================================
# write a program to concatenate a list and a tuple
# =============================================================================
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'uppu', 98]
tuple1 = (1, 2.2, 3.334565, 5, 22, 22, 33, 22, 'dfgsrfgr', 'afadfd')
ans = list1 + list(tuple1)
ans2 = tuple(list1) + tuple1
print(ans)
print(ans2)

# %%
# =============================================================================
# Write a program to find the larger amongst any
# two given numbers.
# =============================================================================

print("Enter First Number")
a = float(input())
print("Enter Second Number")
b = float(input())
if a > b:
    print("Larger Value= ", a)
else:
    print("Larger Value=", b)

# %%
print("Enter First Number")
a = float(input())
print("Enter Second Number")
b = float(input())
if a > b:
    print("Larger Value= ", a)
    print("In Side IF-block")
else:
    print("Larger Value=", b)
    print("In Side ELSE-block")
print("END OF PROGRAM")
# indentation will resolve the membership issue ...
# it will tell the system the control of which line of code belongs to which part

# %%
# =============================================================================
# Wrtite a program to read a character. If, the entered character is
# uppercase, convert it to its lowercase equivalent and vice versa.
# Also generate an error, if the input is anything other than a
# character
# =============================================================================
print("Enter any character")
c = input()
if (c >= "A" and c <= "Z"):
    c = c.lower()
    print(
        f"The out for the given Upper case character's will be as follows: {c}")
else:
    if (c >= "a" and c <= "z"):
        c = c.upper()
        print(
            f"The out for the given Lower case character's will be as follows: {c}")
    else:
        raise ValueError('Input should only contain characters')

# %%


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


def mod(x, y):
    if y == 0:
        return "Cannot mod by zero"
    return x % y


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Mod")

choice = input("Enter choice (1/2/3/4/5): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == '5':
    print(num1, "%", num2, "=", mod(num1, num2))
else:
    print("Invalid input")

# %%
# USER INPUT

name = input("Enter your name: ")
print("Hello, " + name + "!")

print("\n")
age = input("Enter your age: ")
age = int(age)  # Convert the input to an integer


print("You will be " + str(age + 1) + " next year.")
print("\n")

x = float(input("Give me a number: "))
o = input("Give me an operator: ")
y = float(input("Give me yet another number: "))

if o == "+":
    print(x + y)
elif o == "-":
    print(x - y)
elif o == "/":
    print(x / y)
elif o == "*":
    print(x * y)
elif o == "**" or o == "^":
    print(x ** y)
else:
    print("Unknown operator.")

# %%
# Python program to demonstrate
# sys.argv
add = 0.0
# Getting the length of command
# line arguments
n = len(sys.argv)
for i in range(1, n):
    add += float(sys.argv[i])
print("the sum is :", add)

# %%
