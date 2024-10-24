class Grandparent:
    color_eyes = "blue"

    def about(self):
        print("About: I am GrandParent")

    def about_myself(self):
        print("About_myself: I am Grandparent")


class Parent(Grandparent):
    def about_myself(self):
        print("About_myself: I am Parent")


class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()


nick = Child()
