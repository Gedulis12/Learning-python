spam = [0, 1, 2, 3, 4, 5]
cheese = spam #Changing 'cheese' list will result in changing 'spam' list, unlike with variables
cheese[1] = 'Hello!'
print(spam)
print(cheese)