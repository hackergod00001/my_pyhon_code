import pyfiglet


def add(x, y):
    d = x+y
    return d


def sub(x, y):
    d = x-y
    return d


def mul(x, y):
    d = x*y
    return d


def div(x, y):
    d = x/y
    return d


# Add a pretty banner
banner = pyfiglet.figlet_format("Operations_Playground")
print(banner)
while (True):
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5. EXIT")
    choice = int(input("Enter your Choice: "))
    a = float(input("Enter first value: "))
    b = float(input("Enter second value: "))
    if choice == 1:
        c = add(a, b)
        print("The sum of the two numbers is", c)
    elif choice == 2:
        c = sub(a, b)
        print("The sub of the two numbers is", c)
    elif choice == 3:
        c = mul(a, b)
        print("The mul of the two numbers is", c)
    elif choice == 4:
        c = div(a, b)
        print("The div of the two numbers is", c)
    else:
        print("TERMINATING")
        break
