# Python program to  make a simple calculator

# For Addition of Two Numbers
def add(x, y):
    return x + y

# For Substraction of Two Numbers
def substract(x, y):
    return x - y

# For Multiplication of Two Numbers
def multiplication(x, y):
    return x * y

# For Division of Two Numbers
def division(x, y):
    return x / y

print("Select Operation: ""\n""1. Addition""\n""2. Substraction""\n""3. Multiplication""\n""4. Division")
# print("1. Addition")
# print("2. Substraction")
# print("3. Multiplication")
# print("4. Division")

while True:
    choice = input("Enter the choice:")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", substract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplication(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))

        # Check if user wants another calculation break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no)")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")