digit1 = float(input("Please input first digit: "))

operation = input("Please input operation (+, -, *, /): ")

digit2 = float(input("Please input second digit: "))

if operation == "+":
    result = digit1 + digit2
elif operation == "-":
    result = digit1 - digit2
elif operation == "*":
    result = digit1 * digit2
elif operation == "/":
    if digit2 == 0:
        print("Error!!! you can't divide by zero")
        exit()
    result = digit1 / digit2
else:
    print("Invalid operation!")
    exit()
print(f"Result: {result}")