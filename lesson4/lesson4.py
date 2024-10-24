class Human(object):
    height = 185


class Student(Human):
    money = 50


class Worker(Human):
    money = 200


class ITStepStudent(Student):
    crystals = 500


student = Student()
worker = Worker()
its_step = ITStepStudent()

print(student.height)
print(student.money)
print("=======")
print(worker.height)
print(worker.money)
print("=======")
print(its_step.height)
print(its_step.money)
print(its_step.crystals)