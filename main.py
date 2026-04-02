from calculator import add, subtract, multiply, divide

print("=== Simple Calculator ===")

# Get user input for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display operation options
print("\nChoose an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

# Get operation choice
operation = input("\nEnter operation (1/2/3/4): ")

# Perform calculation based on choice
if operation == "1":
    result = add(num1, num2)
    print(f"\nResult: {num1} + {num2} = {result}")
elif operation == "2":
    result = subtract(num1, num2)
    print(f"\nResult: {num1} - {num2} = {result}")
elif operation == "3":
    result = multiply(num1, num2)
    print(f"\nResult: {num1} * {num2} = {result}")
elif operation == "4":
    result = divide(num1, num2)
    print(f"\nResult: {num1} / {num2} = {result}")
else:
    print("\nInvalid operation choice!")
