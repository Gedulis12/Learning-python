import random
secretnumber = random.randint(1,20)

print('Sugalvojau skaičių nuo 1 iki 20')

for guessestaken in range(1, 7):
    print('Pabandyk atspėti :)')
    guess = int(input())

    if guess < secretnumber:
        print('Ne, varliagyvi, mano skaičius didesnis')
    elif guess > secretnumber:
        print('Roplį, tu neteisus, mano skaičius mažesnis')
    else:
        break

if guess == secretnumber:
    print('Šaunuolis žinduoli, atspėjai skaičių iš ' + str(guessestaken) +' karto ir laimėjai!')
else:
    print('Neatspėjai, tu tikras šaltakraujis varliagyvis!')