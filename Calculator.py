#defining the main function to calculate
def calculate():

    #operaton input determines the if statement to run
    operation = input('''
    Please type in the math operation you would like complete:
    + for addition
    - for subtraction
    * for muliplication
    / for division
    ''')

    number_1 = int(input('Enter your first number: '))  #int requires it to be a intiger
    number_2 = int(input('Enter your second number: '))


    #Addition
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))  #String formater to see the numbers in output
        print(number_1 + number_2)

    #Subtraction
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2)) 
        print(number_1 - number_2)

    #Multiplication
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2)) 
        print(number_1 * number_2)

    #Division
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2)) 
        print(number_1 / number_2)

    else:
        print('You have entered an invalid operator.')

    #adding again() to the end of calculate function so it can be called
    again()

def again():
    #Take imput from user
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')

    #If user types y or Y by using str.upper() then run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    #If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print ('See you later.')

    #If user tpyes another key, run the function again
    else:
        again()
#call calculate() outside the function
calculate()                