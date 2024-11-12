

# __call__()

class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, work):
        return f"Inner work = {self.work}. Outer work = {work}"


helper = Helper("homework")
print(helper("cleaning"))