# A decorator is a design pattern in python that allows a user to add new functionality to
# an existing object without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate.

# Example 1: Normal Function
def compute(x):
    return x+5


answer = compute(12)
print(answer)

# OUTPUT
# 17

# %%
# Example 2: Basic Decorator


def compute(x):
    return x+5


calculate = compute

ans = compute(12)
ans1 = calculate(29)
print(ans)
print(ans1)

# OUTPUT
# 17
# 34

# %%


def say(func):
    def employer():
        print("Say Something about you")

    def say_name():
        print("My Name is UPMANYU JHA")

    def say_nationality():
        print("I am from India")

    def wrapper():
        employer()
        say_name()
        say_nationality()
        func()
    return wrapper


@say
def starting_interview():
    print('Real Interview Started')


starting_interview()

# OUTPUT
# Say Something about you
# My Name is UPMANYU JHA
# I am from India
# Real Interview Started

# %%
# divide and conroe is used in recursion -(i.e calling function within it self)

# write a program to calculate factorial of a n no.
# using the above method


def facto(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return (n*facto(n-1))


print("ENTER NUMBER\n")
n = int(input())
ans = facto(n)
print("\nANSWER=", ans)

# %%
