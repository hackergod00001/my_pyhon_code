import pyfiglet


def swap(a, b):
    a, b = b, a
    print("\nAfter Swapping")
    print("a = ", a)
    print("b = ", b)


# Add a pretty banner
banner = pyfiglet.figlet_format("Swap_no._v2")
print(banner)
a = int(input("Enter 1st value: "))
b = int(input("Enter 2nd value: "))
print("a = ", a)
print("b = ", b)
swap(a, b)
