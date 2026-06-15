name = input("Hey there! What's your name? ")       # Asking for user's name

def greet_user(name):                               # Our given function
    if name != None:
        return f"Hello, {name}! Welcome!"           # If a name is given, return a greeting that includes their name
    elif name == None:
        return f"Hello! Welcome!"                   # If a name is given, return a basic greeting
    
print(greet_user(name))                             # Printing the function with parameter

print()

a = int(input("What's the first number? "))         # Asking for two inputs for our sum function
b = int(input("What's the second number? "))
def add_two_numbers(a, b):                          # Two parameters
    return a + b                                    # Returning a sum of the two inputs

sum = add_two_numbers(a, b)                         # Can define the function as a variable and then call it in a print() statement
print(f"The sum of the two numbers is {sum}")

print()

num = int(input("Give me a number and we'll check if it's even: "))
def is_even(num):
    if num % 2 == 0:                                # Checking given number to see if it is even; gives true statement
        return f"{True}, the number is even."
    else:                                           # Otherwise output is false
        return f"{False}, the number is odd."
    
print(is_even(num))