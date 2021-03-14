print('Enter the word: ')

#setting up
word = input()

print('Guess the letter: ')

guesses = ''

turns = 7

while turns > 0:
	failed = 0
	for char in word:
		if char in guesses:
			print(char, end=' ')
		else:
			print('_', end=' ')
			failed += 1

	if failed == 0:
		print('You win')
		print('The word is:', word)
		break

	guess = input('guess the letter: ')
	guesses += guess
	
	if guess not in word:
		turns -= 1
		print('wrong')
		print('You have', + turns, 'more guesses')

		if turns == 0:
			print('you loose!')