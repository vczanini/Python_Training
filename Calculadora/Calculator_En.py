#Vinícius C. Zanini - 2022
#Creating a basic calculator

#Addition of 2 numbers
def Add(x, y):
    return x + y

#Subtract 2 numbers
def Subtract(x, y):
    return x - y

#Divide 2 numbers
def Divide(x, y):
    return x / y

#Multiplie 2 numbers
def Multiply(x, y):
    return x * y

#Function to Choose the numbers and the function used
def Calculation():
    #Show the Possible operation
    print("\nWellcome to the Calculator!")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Division")
    print("4: Multiplication")
    #Take the user input
    Choice = input("Choose the operation that you want: ")
    
    #Check if the choice is Valid
    if Choice in ("1", "2", "3", "4"):
        Number1 = input("Enter the first number: ")
        Number2 = input("Enter the second number: ")
        #Check if the input is an actual number
        #if not go to the again function
        if Number1.isdigit() == False:
            print("Number1 is not a numbeR.")
            Again();
        if Number2.isdigit() == False:
            print("Number2 is not a number.")
            Again()
        
        #Turn the input into a float    
        Number1 = float(Number1)
        Number2 = float(Number2)
        
        #Send the numbers choosen to right function and print the result
        if Choice == '1':
            Addtion = Add(Number1, Number2)
            print(Number1, "+", Number2, "=", Addtion)
        elif Choice == '2':
            Subtraction = Subtract(Number1, Number2)
            print(Number1, "-", Number2, "=", Subtraction)
        elif Choice == '3':
            Division = Divide(Number1, Number2)
            print(Number1, "/", Number2, "=", Division)
        elif Choice == '4':
            Multiplication = Multiply(Number1, Number2)
            print(Number1, "*", Number2, "=", Multiplication)
    else:
        print("Invalid input.")
    #After the run send to the Again function
    Again()

#See if the user wants another operation
#If it does send to the Calculation again, if not finish the code
def Again():
    Calculate = input("Do you want to do another operation? (Y/N): ")
    if Calculate.upper() == 'Y':
        Calculation()
    elif Calculate.upper() == 'N':
        print("GoodBye!")
    else:
        #If the user uses an invalid char/string starts over
        print("Invalid Input.")
        Again()
       
        

#Start the code
Calculation()
    
    