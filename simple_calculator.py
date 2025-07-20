def calculator():
    print("\n🧮 Welcome to the Simple Calculator")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Choose operation: +  -  *  /  %  **")
        op = input("Enter operation: ")

        result = None
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2 if num2 != 0 else "❌ Cannot divide by zero"
        elif op == '%':
            result = num1 % num2
        elif op == '**':
            result = num1 ** num2
        else:
            result = "❌ Invalid Operation"

        print(f"Result: {result}")
    except ValueError:
        print("⚠️ Please enter valid numbers.")

# Start the calculator
if __name__ == "__main__":
    calculator()
