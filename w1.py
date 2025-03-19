# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.


def calculator():
    while True:
        try:
            num1 = int(input('Enter the first number: '))
            num2 = int(input('Enter the second number: '))
            break  
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    operation = input('Enter a valid operation (+, -, *, /, //, %, **): ')

   
    if operation == '+':
        calculationAnswer = num1 + num2
    elif operation == '-':
        calculationAnswer = num1 - num2
    elif operation == '*':
        calculationAnswer = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print(" Error: Division by zero is not allowed.")
            return
        calculationAnswer = num1 / num2
    elif operation == '//':
        if num2 == 0:
            print(" Error: Division by zero is not allowed.")
            return
        calculationAnswer = num1 // num2
    elif operation == '%':
        calculationAnswer = num1 % num2
    elif operation == '**':
        calculationAnswer = num1 ** num2
    else:
        print("Operation not valid. Please enter a valid operation.")

    
    print(f'{num1} {operation} {num2} = {calculationAnswer}')

# Run the calculator
calculator()
