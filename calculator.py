def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("It is not possible to divide by zero.")

while True:
    try:
        input_value = input("Enter the first number (or 'exit' to quit): ")
        if input_value.lower() == 'exit':
            print("Program terminated.")
            break
        num1 = float(input_value)
        
        while True:
            try:
                input_value = input("Enter the second number (or 'exit' to quit, 'back' to restart): ")
                if input_value.lower() == 'exit':
                    print("Program terminated.")
                    break
                if input_value.lower() == 'back':
                    break
                num2 = float(input_value)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        if input_value.lower() == 'back': 
            continue
        
        if input_value.lower() == 'exit':
            break

        while True:
            try:
                operation = input("Choose an operation: (+, -, *, /) or 'exit' to quit, 'back' to restart: ")
                if operation.lower() == 'exit':
                    print("Program terminated.")
                    break
                if operation.lower() == 'back':
                    break
                
                match operation:
                    case "+":
                        print(num1 + num2)
                    case "-":
                        print(num1 - num2)
                    case "*":
                        print(num1 * num2)
                    case "/":
                        print(num1 / num2)
                    case _:
                        print("Invalid operation.")
                        continue
                break
            except Exception as e:
                print("It is not possible to divide a number by zero.")
                continue
        
        if operation.lower() == 'back':
            continue
            
    except ValueError:
        print("Invalid input. Please enter a number.")
