# name = 15
# print(type(name))

my_list = [1, 2, 3, 4, 5]

for method in dir(my_list):
    print(method)

print("=======================")

for method in dir():
    print(method)

print("=======================")

name = "Jack"
print(hasattr(name, "reverse"))
print(hasattr(name, "index"))

print("=======================")
print(getattr(name, "startswith"))
print(getattr(name, "startswith", None))
print(getattr(name, "reverse", None))

print("=======================")

def my_function():
    pass

print(callable(name))
print(callable(my_function))

print("=======================")

class FatherClass:
    pass


class NewClass(FatherClass):
    pass

new_class = NewClass()


print(isinstance(new_class, FatherClass))
print(isinstance(new_class, NewClass))