def info(s, *names):  # variable length arguments
    print("Information about: ", s)
    for i in names:
        print(i)

# s is like a normal variable, *names is like a pointer in c/c++ as here memory is added dynamically


info("food", "Italian", "mexican", "turkish")
print("=====================================")
info("car", "Mercedes", "BMW", "Audi", "Jaguar", "Ford")
print("=====================================")
info("cities", "Mumbai", "London", "Paris", "New York", "Barcelona", "Moscow")


# #OUTPUT
# Information about:  food
# Italian
# mexican
# turkish
# =====================================
# Information about:  car
# Mercedes
# BMW
# Audi
# Jaguar
# Ford
# =====================================
# Information about:  cities
# Mumbai
# London
# Paris
# New York
# Barcelona
# Moscow
