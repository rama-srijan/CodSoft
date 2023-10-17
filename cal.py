def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def calculator():
    while True:
        choice = input("Enter the operation number (+,-,*,/): ")
        if choice not in ['+', '-', '*', '/']:
            print("Invalid choice. Please try again.")
        else:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice == '+':
                result = add(num1, num2)
            elif choice == '-':
                result = subtract(num1, num2)
            elif choice == '*':
                result = multiply(num1, num2)
            else:
                result = divide(num1, num2)
            print("Result:", result)
            break
if __name__ == "__main__":
    calculator()
