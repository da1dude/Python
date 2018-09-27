num1 = int(input('Please enter a number: ')) #only allows intigers for input: int()
divNum = int(input('Please enter a number to divide by: '))


if num1 % 4 == 0:
    print('The number is diviisible by 4')
else:
    print('The number is not divisible by 4')


if num1 % 2 == 0:
    print(num1,' is even!')
elif num1 % divNum == 0:
    print(num1,' divides evenly!') #this is wrong
else:
    print(num1,' is odd!')   