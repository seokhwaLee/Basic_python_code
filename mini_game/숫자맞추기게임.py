#This is a guess the number game.

myName = input('Hello! What is your name? ')

number = 5
print('Well, '+myName+', I am thinking of a number between 1 and 20. ')
guess = int(input('Take a guess : '))
print('com :', number, 'you :',guess)

if guess != number:
    print ('Your guess is wrong')
    
if guess == number:
    print('Good job. ' + myName + '! You guessed my number! ')
