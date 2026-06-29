def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y
def power(x, y):
    return x ** y
def calculator():
    print("--- Mid-Level Python Calculator ---")
    print("Operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Exit")
    while True:
        choice = input("\nEnter operation number (1-6): ")
        if choice == '6':
            print("Program terminated. Goodbye!")
            break
        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error! Please enter valid numbers.")
                continue
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")
        else:
            print("Invalid choice! Please select a number between 1 and 6.")
# Run the calculator
if __name__ == "__main__":
    calculator() 
