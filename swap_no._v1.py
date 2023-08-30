def swap(x, y):
    x = x+y
    y = x-y
    x = x-y
    print("After Swapping\n")
    print("\na= ", x)
    print("\nb= ", y)


a = int(input("Enter 1st value: "))
b = int(input("Enter 2nd value: "))
print("\na= ", a)
print("\nb= ", b)
swap(a, b)
