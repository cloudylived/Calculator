print("Welcome to Cloudy's Calculator, let's get started!")

calculator_on = True

while calculator_on:

    continue_choice_valid = False 

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

            elif operation == "**":
                operation_valid = True

            else:
                print("Invalid operation. Please choose from the following: + - * /")

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

    elif operation == "**":
        answer = number1 ** number2
        calculation_valid = True

    if calculation_valid:
        print(answer)
    
    while not continue_choice_valid:
            
       continue_choice = input("New calculation? (y/n): ")
     
       if continue_choice == "n":
            continue_choice_valid = True
            calculator_on = False

       elif continue_choice == "y":
           continue_choice_valid = True
    
       else:
           print("Invalid input. Please choose either 'y' or 'n' .")
        

print("Thank you for using Cloudy's Calculator!")
 

       
        

 
