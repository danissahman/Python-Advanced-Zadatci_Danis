def calculator(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    else:
        raise ValueError(f"Unknown operator {operator}. Allowed operators are: +, -, *, /.")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    op = input("Enter arithmetic operator (+, -, *, /): ")

    result = calculator(num1, num2, op)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Error (ValueError): Invalid number or operator: ({e})")
except ZeroDivisionError:
    print(f"Error (ZeroDivisionError): Cannot divide by zero.")
except Exception as e:
    print(f"Error (Exception): An unknown error has occurred: ({e})")
finally:
    print("End of program.")