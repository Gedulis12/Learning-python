def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    numberinput = int(input('Enter number: '))

    while True:
        c = collatz(numberinput)
        if c != 1:
            numberinput = c
            print(numberinput)
        else:
            print(1)
            break
except ValueError:
    print('You must enter an integer.')