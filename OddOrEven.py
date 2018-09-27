num1 = int(input('Please enter a number: ')) #only allows intigers for input: int()
check = num1 % 2 # Mudelo % checks if there is a remainder based on the number dividing it. In this case 2 to check if even or odd

if check == 0:
    print('The number is even!')
else:
    print('The number is odd!')