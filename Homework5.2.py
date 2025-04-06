while True:
    print("Choose your operation:")
    print("1. Plus")
    print("2. Minus")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose your operation (1/2/3/4): ")

    try:
        digit1 = float(input("Input first digit: "))
        digit2 = float(input("Input second digit: "))
    except ValueError:
        print("Please enter correct digits.")
        continue

    if choice == '1':
        result = digit1 + digit2
        print(f"Result: {digit1} + {digit2} = {result}")
    elif choice == '2':
        result = digit1 - digit2
        print(f"Result: {digit1} - {digit2} = {result}")
    elif choice == '3':
        result = digit1 * digit2
        print(f"Result: {digit1} * {digit2} = {result}")
    elif choice == '4':
        if digit2 == 0:
            print("Error divide by zero")
            continue
        result = digit1 / digit2
        print(f"Result: {digit1} / {digit2} = {result}")
    else:
        print("Wrong choice of operation.")
        continue

    continue_choice = input("Would you like to perform another calculation?? (yes/y to continue): ").lower()
    if continue_choice not in ('yes', 'y'):
        print("Thank you for using this program")
        break