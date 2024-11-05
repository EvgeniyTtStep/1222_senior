my_colors = ['red', 'green', 'blue']

iterator = iter(my_colors)

# print(next(iterator)) # red
# print(next(iterator))
# print(next(iterator))


print("Start for:")
for color in iterator:
    print(color)

print("Start new for:")
for color in iterator:
    print(color)


class Counter:
    def __init__(self, max_num):
        self.i = 0
        self.max_num = max_num

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_num:
            raise StopIteration
        return self.i


counter = Counter(5)

print(next(counter))
print(next(counter))

for count in counter:
    print(count)




