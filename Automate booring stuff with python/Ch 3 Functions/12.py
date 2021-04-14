def collatz(number):
    while number != 1:
        if number % 2 == 0: #this is an even number
            number = number // 2
            print(number)
        elif number % 2 == 1: #this is an odd number
            number = 3 * number + 1
            print(number)
        elif number == 1:
            print(number)
        
    return ''

print('Enter number:')
try:
    print(collatz(int(input())))
except ValueError:
    print('You must enter an integer.')