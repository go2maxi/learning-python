# Trying to understand how iteration actually works in Python

numbers = [1, 2, 3]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))

# print(next(it))  # raises StopIteration

class CountUp:
    def __init__(self, max_value):
        self.current = 0
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max_value:
            raise StopIteration
        self.current += 1
        return self.current


counter = CountUp(3)

for n in counter:
    print(n)

# At first this felt more complicated than it needed to be

# Personal note: understanding the iterator protocol made for-loops feel much less "magical".

