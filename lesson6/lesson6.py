# print(10 / 0)

print(type(ZeroDivisionError), issubclass(ZeroDivisionError, BaseException))
print("=========================")


try:
    print("Before error")
    print(name)
    print("After error")
except:
    print("Ooops ")

print("=========================")



# try:
#     print(10/0)
# except NameError:
#     print("Its a NameError")
# except ZeroDivisionError:
#     print("Its a ZeroDivisionError")
print("=========================")


try:
    print(10/0)
except (NameError, ZeroDivisionError) as error:
    print("Its a NameError or ZeroDivisionError = ", error)

print("=========================")

try:
    try:
        print(hello)
    except SyntaxError:
        print("Syntax Error")
except NameError as error:
    print("Name Error =", error)

print("=========================")

try:
    print("Has errors")
    print(asfsdf)
except:
    print("Except")
else:
    print("Else")
finally:
    print("Finally")

print("=========================")


print("End program!")
