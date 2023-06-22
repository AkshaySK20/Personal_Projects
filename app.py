def divider(a, b):
    return a / b
    # TODO


a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
try:
    c = divider(a, b)
    print(f"The answer is {c}")
except:
    print("You cannot divide by zero")
finally:
    print("Processed")
