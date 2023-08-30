# Write a program to read the age of the person and determine the ticket cost.
# If the age is less than 2 yrs, no ticket is needed.
# For all children between 2 years and 13 years of age, child fare applicable,
# In all other case full adult fare is applicable.

import qrcode
import calendar
print("Enter AGE")
age = int(input())
if age < 2:
    print('You are a baby so No Ticket Required')
elif 2 <= age < 13:
    print('You are an toddler so Child Fare Applicable')
else:
    print("Adult Fare Applicable")


# %%

# Write a program to display the table of any given value till 10.
num = int(input("PLease Enter the number: \n"))

for i in range(1, 11):
    print(f'{num}*{i}={num*i}')

# or
# %%
num = int(input("PLease Enter the number: \n"))

for i in range(1, 10):
    print(f'{num}*{i}={num*i}')
print(f'{num}*{i}={num*i}')
# or
# %%
num = int(input("Please Enter the number: \n"))
i = 1
while i <= 10:
    multiplication = num * i
    print(f'{num}*{i}={multiplication}')
    i += 1  # Increment i by 1 in each iteration


# %%
# Write a program to calculate the following series 1+1/2**2+1/3**2 ... till n terms.
n = int(input("\nPLEASE ENTER THE TERMS COUNT i.e VALUE OF N\n"))
i = 1
result = 0.0
while i <= n:
    term = 1/pow(i, 2)
    result += term
    print(f'1/{i}**2 = {term}')
    i += 1

print(f"The sum of 1 + ... + 1/{n}^2 is: {result}")

# or
# %%
n = int(input("\nPLEASE ENTER THE TERMS COUNT i.e VALUE OF N\n"))
result = 0.0
for i in range(1, n+1):
    result += 1/pow(i, 2)

print(f"The sum of 1 + ... + 1/{n}^2 is: {result}")

# %%
# Write a program to create a dictionary and iterate through it using a for statement.
# Display the value corresponding to all the keys.
d = {"1": "Mango", "2": "Apple", "3": "cherry"}
for i in d:
    print(f'Current value of i= {i}')
    print(d[i])

s = "same to save"
for i in s:
    if i == 's':
        print("This is 's'")

# %%
# Write a program to display the following pattern
# *
# **
# ***
# ****
# :
# (n rows)
n = int(input("\nPLEASE ENTER NO. OF ROWS NEEDED\n"))
a = "*"
for i in range(0, n+1):
    print(a*i)

# %%
# Write a program to calculate the factorial (i.e 6!, 5!,x!...) of a given
# number using a while loop.
n = int(input("Enter the no.:\n"))
i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1
print(f'{n}! factorial is: {fact}')

# %%
# or

n = int(input("Enter the no.:\n"))
fact = 1
while n > 0:
    fact *= n
    n -= 1
print(f'{n}! factorial is: {fact}')

# %%
# While -else loop
n = int(input("Enter the no.:\n"))
fact = 1
while n > 0:
    fact *= n
    n -= 1
else:
    # else block will execute only when the condition becomes false
    print("THIS IS WHILE ELSE")
print(f'{n}! factorial is: {fact}')

# %%
# Write a program to accept three digits and print all
# possible combinations from the digits.

n1 = int(input("Enter the 1st no.:\n"))
n2 = int(input("Enter the 2nd no.:\n"))
n3 = int(input("Enter the 3rd no.:\n"))
if ((9 >= n1 >= 0) & (9 >= n2 >= 0) & (9 >= n3 >= 0)):
    for i in (n1, n2, n3):
        for j in (n1, n2, n3):
            for k in (n1, n2, n3):
                if ((j != k) & (j != i) & (k != i)):
                    print("{} {} {}".format(str(i), str(j), str(k)))


# %%
# OR
n1 = int(input("Enter the 1st no.:\n"))
n2 = int(input("Enter the 2nd no.:\n"))
n3 = int(input("Enter the 3rd no.:\n"))
d = []
d.append(n1)
d.append(n2)
d.append(n3)
# print(d)
for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            if ((j != k) & (j != i) & (k != i)):
                print(d[i], d[j], d[k])


# %%
# write a program to create two lists of length n1 and n2
# respectively and merge them

n1 = int(input("enter values for list n1"))
n2 = int(input("enter values for list n2"))
list1 = []
list2 = []
for i in range(0, n1+1):
    ele = int(input())
    # adding the element
    list1.append(ele)

for i in range(0, n2+1):
    ele = int(input())
    # adding the element
    list2.append(ele)
list3 = list1 + list2
print(f'merge form of list1 + list2 = {list3}')

# %%
# write a program to create a list and sort the elements inside it.
n = int(input("enter values for list n1"))
list1 = []
for i in range(0, n+1):
    ele = int(input())
    # adding the element
    list1.append(ele)
list1.sort()
print(list1)
sorted_list1 = sorted(list1)  # sorting the elements from small to large
print(sorted_list1)

# %%

# Write a program to generate the calender of any month in any given year.
# import calendar
month = int(input('enter the number of months'))
year = int(input('enter the year'))
print(calendar.month(year, month))

# %%

# Link for website
input_data = "<ENTER YOUR URL>"
# Creating an instance of qrcode
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('hackergod00001.png')

# %%
