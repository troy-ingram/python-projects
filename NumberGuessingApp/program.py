import random

print('------------------------------------')
print('      GUESS THE NUMBER APP')
print('------------------------------------')
print('')

hidden_number = random.randint(0, 100)
guess = -1
user_name = input('What is your name?: ')

while guess != hidden_number:
    guess = int(input("What is your guess?: "))
    if guess > hidden_number:
        print('Sorry {}, {} is too HIGH. Please try again'.format(user_name, guess))
    elif guess < hidden_number:
        print('Sorry {}, {} is too LOW. Please try again'.format(user_name, guess))
    else:
        print('Congratulations {}! {} is correct!'.format(user_name, guess))
    
    
    
