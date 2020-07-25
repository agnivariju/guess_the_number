# guess the number
# no of guesses allowed = 5
# print won or game over
# if won print the no of guesses to say the correct answer
print('This is a number guessing game developed by Agniva Chakraborty\n')
print('Your task is to guess the number\n')
n = 18
number_of_guesses = 1
print("Number of guesses is only limited to 10")
while(number_of_guesses <= 10):
    guess_the_number = int(input('Guess the number:\n'))
    if guess_the_number > 18:
        print('Oops your number is too high. Try again !\n')
    elif guess_the_number < 18:
        print('Oops your number is too low. Try again !\n')
    else:
        print('Congratulations, You Won !\n')
        print('You took', number_of_guesses, 'number of guesses to finish.')
        break
    print(10-number_of_guesses, 'number of guesses left')
    number_of_guesses = number_of_guesses+1

if number_of_guesses > 10:
    print('Game Over !')
