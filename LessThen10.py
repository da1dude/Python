a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num1 = int(input('Please enter a number: '))

newList = []


# i is the index of a, it runs through a's list and follows the if statement
# it then appends what is found in a's list to the new list
for i in a:
    if i < num1:
        newList.append(i)
        
print(newList)
