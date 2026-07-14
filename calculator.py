print("Welcome to Cloudy's Calculator, let's get started!")

calculator_on = True

while calculator_on:

    number_input_valid = False

    while not number_input_valid:
        try:
            number1 = float(input("First number: "))  
            number_input_valid = True

        except:
            print("Please enter a number")

    number_input_valid = False

    while not number_input_valid:
        try:
            number2 = float(input("Second number: "))
            number_input_valid = True

        except:
            print("Please enter a number")

    operation_valid = False
    calculation_valid = False

    while not operation_valid:
            operation = input("Operation: ")

            if operation == "+":
                operation_valid = True

            elif operation == "-":
                operation_valid = True

            elif operation == "*":
                operation_valid = True

            elif operation == "/":
                operation_valid = True

            else:
                print("Invalid operation, try again")

    if operation == "+":
        answer = number1 + number2
        calculation_valid = True

    elif operation == "-":
        answer = number1 - number2
        calculation_valid = True

    elif operation == "*":
        answer = number1 * number2
        calculation_valid = True

    elif operation == "/":
        if number2 == 0:
            print("Error: Cannot divide by zero")
        else:
            answer = number1 / number2
            calculation_valid = True

    if calculation_valid:
        print(answer)
    
    continue_choice = input("New calculation? (y/n): ")

    if continue_choice == "n":
        calculator_on = False

    

 
