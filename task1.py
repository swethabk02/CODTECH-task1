def calculator():
    print("Welcome to the basic calculator!")

    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
        
        if operation == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        elif operation == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation selected. Please try again.")
        
        another = input("Do you want to perform another operation? (yes/y or no/n): ").strip().lower()
        if another not in ('yes', 'y'):
            break

    print("Thank you for using the basic calculator!")
calculator()

