#!/bin/bash

# print string
print("Hello, World!")
print('Hello, World!')
print("""This string runs
__________multiple lines""")  # triple quote for multiple lines
print("This string is"+"Awesome")  # we can also concatenate
print("\n")  # new line
print("test that new line out")
my_string = "Hello, World!"
print(my_string[0])
print(len(my_string))  # String Length
substring = my_string[7:12]
print(substring)  # String Slicing
print(my_string.upper())
print(my_string.lower())
print(my_string.strip())
print(my_string.split())
# print(my_string.replace())
name = 'Alice'
age = 30
print("My name is %s and I'm %d years old." % (name, age))


print("\n")  # new line
# Math
print(50+50)  # add
print(50-50)  # substract
print(50*50)  # multiply
print(50/50)  # divide
print(50**2)  # exponents
print(50 % 50)  # moduls -remainder
print(50-50+50*50/50 % 50)
print(50//6)
print(50/6)
print(50 + 50 - 50 * 50 / 50)  # PEMDAS
print(50 ** 2)  # exponents
print(50 % 6)  # modulo - takes what is left over
print(50 / 6)  # division with decimals
print(50 // 6)  # no remainder
# Output: My name is Alice and I'm 30 years old.


print("\n")  # new line
# Variables and Methods
quote = "All is fair in love and war."
print(quote)

print(quote.upper())  # uppercase
print(quote.lower())  # lowercase
print(quote.title())  # title case
print(len(quote))  # counts characters


name = "Upmanyu"  # string
age = 100  # int
gpa = 3.7  # float - has a decimal

print(int(age))
print(int(30.1))
print(int(30.9))  # - Will it round? No!

print("My name is " + name + " and I am " + str(age) + " years old.")


age += 1
print(age)

birthday = 1
age += birthday
print(age)

# Variable assignment
x = 10
name = "John"
is_true = True

print("\n")
# Variable usage
y = x + 5
print("Hello, " + name)
if is_true:
    print("The condition is true")

print("\n")
# Built-in method example
numbers = [1, 2, 3, 4, 5]
length = len(numbers)
print("Length:", length)


# User-defined method example
def greet(name):
    print("Hello, " + name)


greet("Alice")


print("\n")
# Functions
print("Here is an example function:")


def who_am_i():  # this is a function without parameters
    name = "upmanyu"
    age = 100  # local variable
    print("My name is " + name + " and I am " + str(age) + " years old.")


who_am_i()

# adding parameters


def add_one_hundred(num):
    print(num + 100)


add_one_hundred(100)

# multiple parameters


def add(x, y):
    print(x + y)


add(7, 7)


def multiply(x, y):
    return x * y


multiply(7, 7)
print(multiply(7, 7))


def square_root(x):
    print(x ** .5)


square_root(64)


def greet():
    print("Hello, World!")


greet()


def greet(name):
    print("Hello, " + name + "!")


greet("Alice")


def add_numbers(a, b):
    return a + b


result = add_numbers(3, 4)
print(result)  # Output: 7


def nl():
    print('\n')


nl()


x = 5
y = 10


# Relational operators
print(x == y)   # Output: False
print(x < y)    # Output: True


# Boolean expressions
print(x < y and y > 0)    # Output: True
print(x < y or y < 0)     # Output: True
print(not (x == y))       # Output: True

nl()

# Boolean expressions (True or False)
print("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()

# Relational and Boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = True and True  # True
test_and2 = True and False  # False
test_or = True or True  # True
test_or2 = True or False  # True

test_not = not True  # False

nl()
# if condition:
# code to be executed if the condition is true

x = 5
if x > 0:
    print("x is positive")

x = 5
if x > 0:
    print("x is positive")
else:
    print("x is not positive")


x = 5
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

nl()
# Conditional Statements


def drink(money):
    if money >= 2:
        return "You've got yourself a drink!"
    else:
        return "No drink for you!"


print(drink(3))
print(drink(1))


def bev(age, money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money."
    elif (age < 21) and (money >= 5):
        return "Nice try, kid!"
    else:
        return "You're too poor and too young!"


print(bev(21, 5))
print(bev(21, 4))
print(bev(20, 5))
print(bev(20, 4))

nl()

fruits = ["apple", "banana", "orange"]

print(fruits[0])    # Output: "apple"
print(fruits[2])    # Output: "orange"

fruits[1] = "grape"     # Modifying an element
fruits.append("kiwi")   # Adding an element to the end
fruits.remove("apple")  # Removing an element


fruits = ["apple", "banana", "orange"]
fruits2 = ["grape", "kiwi"]


combined = fruits + fruits2
# Output: ["apple", "banana", "orange", "grape", "kiwi"]
print(combined)


print(len(fruits))      # Output: 3


sublist = fruits[1:3]
print(sublist)          # Output: ["banana", "orange"]


for fruit in fruits:
    print(fruit)        # Output: "apple", "banana", "orange"

nl()
# Lists - Have brackets []
movies = ["When Harry Met Sally", "The Hangover",
          "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1])  # returns the second item in the list - index / indices
print(movies[0])  # returns the first item in the list
# returns the first number given until right before last number given
print(movies[1:3])
print(movies[0:4])  # returns all
print(movies[1:])  # returns everything from number to end of list
print(movies[:1])  # everything before 1
print(movies[:2])
print(movies[-1])  # grabs last item

print(len(movies))  # counts items in list
movies.append("JAWS")
print(movies)  # appends to end of list

movies.insert(2, "Hustle")
print(movies)

movies.pop()  # removes last item
print(movies)

movies.pop(0)  # removes first item
print(movies)

amber_movies = ['Just Go With It', '50 First Dates']
our_favorite_movies = movies + amber_movies
print(our_favorite_movies)

grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1] = 83
print(bobs_grade)
nl()

# TUPPLES
fruits = ("apple", "banana", "orange")
print(fruits[0])    # Output: "apple"
print(fruits[2])    # Output: "orange"
# fruits[1] = "grape"    # This will raise an error

fruits = ("apple", "banana", "orange")
fruits2 = ("grape", "kiwi")


combined = fruits + fruits2
print(combined)         # Output: ("apple", "banana", "orange", "grape", "kiwi")


print(len(fruits))      # Output: 3


subtuple = fruits[1:3]
print(subtuple)         # Output: ("banana", "orange")

nl()
# Tuples - Do not change, ()
grades = ("a", "b", "c", "d", "f")

# grades.pop, grades.append won't work - not mutable

print(grades[1])

nl()

# LOOPING
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

count = 0
while count < 5:
    print(count)
    count += 1


nl()
# For loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
    print(x)

# While loops - execute as long as true
i = 1

while i < 10:
    print(i)
    i += 1

nl()

# ADVANCED STRINGS

my_name = "Heath"
print(my_name[0])  # first letter
print(my_name[-1])  # last letter

sentence = "This is a sentence."
print(sentence[:4])

print(sentence.split())  # delimeter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'"  # - show example
print(quote)
quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                       hello          "
print(too_much_space.strip())

print("A" in "Apple")  # returns true
print("a" in "Apple")  # returns false - case sensitive

letter = "A"
word = "Apple"
print(letter.lower() in word.lower())  # improved

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))
print("My favorite movie is %s" % movie)
print(f"My favorite movie is {movie}")

nl()

name = 'Alice'
age = 30
print("My name is %s and I'm %d years old." % (name, age))
# Output: My name is Alice and I'm 30 years old.


nl()


# DICTIONARIES - key/value pairs {}

drinks = {"White Russian": 7, "Old Fashion": 10,
          "Lemon Drop": 8}  # drink is key, price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": [
    "Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
employees['Legal'] = ["Mr. Frond"]  # adds new key:value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]})  # adds new key:value pair
print(employees)

drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian"))

student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}


print(len(student))          # Output: 3


for key in student:
    # Output: "name Alice", "age 20", "major Computer Science"
    print(key, student[key])


del student["age"]           # Deleting a key-value pair
