import random

answer=random.randint(1,100)
counter=0

while True:
    counter+=1
    n=int(input('Guess:'))
    if n>answer:
        print('Too Big.')
    elif n<answer:
        print('Too Small.')
    else:
        print('Yes!')
        break
        
print('You Guessed %d Times'% counter)

if counter>7:
    print('Eeee! So many times!')