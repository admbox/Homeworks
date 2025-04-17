def say_hi(name: str, age: int) -> str:
    return f"Hello,my name is {name} and I am {age} ages."

user_name = input("Please input your name: ")
user_age = int(input("Please input your age: "))

print(say_hi(user_name, user_age))