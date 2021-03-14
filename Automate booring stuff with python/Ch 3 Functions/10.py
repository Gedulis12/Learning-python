import random
print('I am thinking of a number between 1 and 20.')

number = random.randint(1, 20)
guesscount = 0
guess = ''

while guess != number:
    print('Take a guess')
    guess = input()
    guess = int(guess)
    guesscount = guesscount + 1
    if guess > number:
        print('Your guess is too high')
    elif guess < number:
        print('Your guess is too low')
    else:
        break
print('Good job! You guessed my number in ' + str(guesscount) + ' times')