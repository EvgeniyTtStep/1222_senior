import inspect
import requests

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))


class MyClass(object):
    def __init__(self, age, height, name="Jack"):
        self.age = age
        self.name = name
        self.surname = "Lukas"


signature = inspect.signature(MyClass)

for param in signature.parameters.values():
    print(param.name, param.default)
