def generate_cube_numbers(limit):
    n = 2
    while True:
        cube = n ** 3
        if cube >= limit:
            return
        yield cube
        n += 1
try:
    user_limit = int(input("Enter the limit for cubes of numbers: "))
    print("Cubes of numbers are less than", user_limit, ":")
    for number in generate_cube_numbers(user_limit):
        print(number)
except ValueError:
    print("Please enter a valid integer")