from utils.maths import add, subtract, average


def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operation. Please use +, -, *, or /.")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
