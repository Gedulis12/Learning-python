print('whats your name?')
name = input()
print('how old are you?')
age = int(input())
if name == 'Alice' and age > 12 and age < 100:
    print('Hi, Alice')
elif age < 12:
    print('you are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
else:
    print('You are neither Alice nor a little kid.')