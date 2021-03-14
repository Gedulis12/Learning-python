def spam():
    global eggs
    eggs = 'spam' #this is the global

def bacon():
    eggs = 'bacon' #this is a local
    print(eggs)

def ham():
    print(eggs) #this is the global

spam()
print(eggs)
eggs = 42 #this is the global
print(eggs)
spam()
bacon()
print(eggs)
ham()