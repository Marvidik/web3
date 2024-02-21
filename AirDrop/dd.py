     
def perform_division():
    try:

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))


        if num2 == 0:

            raise ZeroDivisionError("Error: Division by zero is not allowed")

        result = num1 / num2
        print("Result of division:", result)

    except ZeroDivisionError as e:
        print(e)


perform_division()



