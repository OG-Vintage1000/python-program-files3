try:
# Defining our basic math functions
    print("We're going to do some basic math here folks.")
    a = int(input("What's the first number? "))
    b = int(input("What's the second number? "))

    # Adding two numbers
    def add(a, b):
        return a + b

    # Subtracting two numbers
    def subtract(a, b):
        return a - b

    # Multiplying two numbers
    def multiply(a, b):
        return a * b

    # Dividing two numbers
    def divide(a, b):
        return a / b
  
# Returning result for each individual operation
    print(f"The sum is {add(a, b)}.")
    print(f"The difference is {subtract(a, b)}.")
    print(f"The product is {multiply(a, b)}.")
    print(f"The division is {divide(a, b)}.")

# Include exceptions here
except(ZeroDivisionError):
    print("Error. Division by 0.")
except:
    print("Error. Incorrect input value.")

print()

try:  
# Choose some numbers and operation
    print("We're doing more basic math.")
    a = int(input("What's the first number? "))
    b = int(input("What's the second number? "))

    op = input("Select an operation: +, -, *, / ")

# Function to determine which math function to use based on operation selected
    def calculate(a, b, op):
        if op == "+":
            return add(a, b)
        elif op == "-":
            return subtract(a, b)
        elif op == "*":
            return multiply(a, b)
        elif op == "/":
            return divide(a, b)
        
    print(f"The result is: {calculate(a, b, op)}.")

except(ZeroDivisionError):
    print("Error. Division by 0 again.")
except:
    print("Error. Incorrect input value.")

# Very basic, but gets the job done