# main.py

def greet_user(name):
    return f"Hello, {name}! Welcome to our program."


def add_numbers(a, b):
    return a + b


def main():
    # Sample function calls
    name = input("Enter your name: ")
    print(greet_user(name))
    
    print("Let's add two numbers.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The sum is: {add_numbers(num1, num2)}")


if __name__ == "__main__":
    main()
