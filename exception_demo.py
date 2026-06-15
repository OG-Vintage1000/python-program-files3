try:
    a = int(input("What's the first number: "))
    b = int(input("What's the second number: "))
    def safe_divide(a, b):
        result = round(a / b, 2)
        return result
    result = safe_divide(a, b)
    print(f"The division is {result}")
except ZeroDivisionError:
    print("Error: cannot divide by 0.")
except:
    print("Please input correct type.")
finally:
    print("Division operation completed.")