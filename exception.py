a = 5
b = 0

try:
    print("Open")
    print(a / b)
except ZeroDivisionError as e:
    print("You cannot divide by zero", e)

finally:
    print("Closed")

print("Thank you")