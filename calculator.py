def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("=== Simple Calculator CLI App ===")
    print("Operations: + (add), - (subtract), * (multiply), / (divide)")
    print("Type 'exit' anytime to quit.\n")

    while True:
        num1 = input("Enter first number: ")
        if num1.lower() == "exit":
            print("Exiting calculator. Goodbye!")
            break

        num2 = input("Enter second number: ")
        if num2.lower() == "exit":
            print("Exiting calculator. Goodbye!")
            break

        operation = input("Enter operation (+, -, *, /): ")
        if operation.lower() == "exit":
            print("Exiting calculator. Goodbye!")
            break

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid input! Please enter numeric values.\n")
            continue

        if operation == "+":
            print("Result:", add(num1, num2))
        elif operation == "-":
            print("Result:", subtract(num1, num2))
        elif operation == "*":
            print("Result:", multiply(num1, num2))
        elif operation == "/":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid operation! Choose from +, -, *, /.")

        print() 


if __name__ == "__main__":
    calculator()
