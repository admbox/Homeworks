def sequence_generator(func, start, n):
    current = start
    count = 0
    while count < n:
        yield current
        current = func(current)
        count += 1

func = lambda x: x * 2
start = 1
n = 5

print("Generated sequence:")
for value in sequence_generator(func, start, n):
    print(value)