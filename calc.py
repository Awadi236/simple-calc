def calculator():
    print("Simple Calculator")
    print("Choose operation: +, -, *, /")
    operation = input("Enter operation: ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        else:
            result = "Invalid operation!"

        print(f"Result: {result}")
    except ValueError:
        print("Invalid input! Please enter numbers.")

if __name__ == "__main__":
    calculator()
