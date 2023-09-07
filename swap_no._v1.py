import pyfiglet


def swap(x, y):
    x = x+y
    y = x-y
    x = x-y
    print("\nAfter Swapping")
    print("a = ", x)
    print("b = ", y)


# Add a pretty banner
banner = pyfiglet.figlet_format("Swap_no._v1")
print(banner)
a = int(input("Enter 1st value: "))
b = int(input("Enter 2nd value: "))
print("a = ", a)
print("b = ", b)
swap(a, b)
