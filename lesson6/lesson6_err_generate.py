def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f'var_1 = {type(var_1)}!!!  must be str')
    else:
        return var_1


# first_var = "Hello"
# checker(first_var)

print("=========================")


class ZacharError(Exception):
    def __str__(self):
        return "yo this is Zachar Error!!!!!!!!!!!!!!!"


def check_zachar(amount, limit):
    if amount > limit:
        return "ok"
    else:
        raise ZacharError(amount)


amount = int(input("Please enter a number: "))
check_zachar(amount, 300)
