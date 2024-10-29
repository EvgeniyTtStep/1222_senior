import requests
# help(requests)

def my_function():
    pass


class MyClass:
    pass


rq = requests
my_f = my_function
jack = MyClass
num = 15

# print(num.__name__)
print(__name__)
print("==================")
print(requests.__name__)
print(rq.__name__)
print("==================")
print(my_function.__name__)
print(my_f.__name__)
print("==================")
print(MyClass.__name__)
print(jack.__name__)
