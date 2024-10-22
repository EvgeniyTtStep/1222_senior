class Student:

    # constuctor
    def __init__(self, first_name="Bob", last_name="Smith"):
        self.first_name = first_name
        self.last_name = last_name

    def show_full_name(self):
        print(self.first_name + ' ' + self.last_name)


student1 = Student('Jack', 'Lukashik')
student2 = Student('Artem', 'Spasoff')
student3 = Student('Glib', 'Illin')
student4 = Student()
student5 = Student(first_name="Kevin", last_name="Shorts")

# print(student1.full_name)
# print(student2.full_name)
# print(student3.full_name)
# print(student4.full_name)

student1.show_full_name()
student2.show_full_name()
student3.show_full_name()
student4.show_full_name()