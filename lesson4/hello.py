class Hello_world(object):
    hello = "public Hello!"
    _hello = "protected Hello!"
    __hello = "private Hello!"
    def __init__(self):
        self.world = "public World!"
        self._world = "protected World!"
        self.__world = "private World!"

    def print_hello(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)


class Hi(Hello_world):
    def print_hello(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
        print(self.__hello)
        print(self.__world)


hello = Hello_world()
hello.print_hello()
print("===============")
hi = Hi()
hi.print_hello()