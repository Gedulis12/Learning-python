spam = ['apples', 'banannas', 'tofu', 'cats', 'eggs', 42]

for i in spam:
    if spam[-1] == i:
        print('and ' + str(i))
    else:
        print(str(i), end=', ')