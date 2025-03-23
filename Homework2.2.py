number = int(input("Please input 5-digit number: "))

first_digit, remainder = divmod(number, 10000) 
second_digit, remainder = divmod(remainder, 1000)  
third_digit, remainder = divmod(remainder, 100)  
fourth_digit, remainder = divmod(remainder, 10)   
fifth_digit = remainder


reversed_number = fifth_digit * 10000 + fourth_digit * 1000 + third_digit * 100 + second_digit * 10 + first_digit

print("Reverse digit:", reversed_number)