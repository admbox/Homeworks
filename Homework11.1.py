def prime_generator(limit):
    for num in range(2, limit):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
try:
    user_input = int(input("Enter the upper limit of the range: "))
    primes = list(prime_generator(user_input))
    print("Prime numbers up to", user_input, ":", primes)
except ValueError:
    print("Please enter a valid integer")