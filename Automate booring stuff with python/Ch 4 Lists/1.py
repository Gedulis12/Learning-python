catnames = []
while True:
    print('Enter the name of cat' + str(len(catnames)+1)+ '(Or enter othing to stop.):')
    name = input()
    if name == '':
        break
    catnames = catnames + [name]
print('the cat names are:')
for name in catnames:
    print(' ' + name)