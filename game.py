import random
import time

def draw(nu_min, nu_max):
    return random.randrange(nu_min, nu_max)

def is_number(number):
    try:
        int(number)
        return 1, int(number)
    except ValueError:
        print('Try agian! This value is incorrect!')
        return 0, 0

def user_numbers():
    while True:
        min = 0
        max = 0
        usr_num = 0
        
        while min == 0:
            nu_min = input('Please enter the minimum range for the game: \n')
            min, nu_min = is_number(nu_min)
        
        
        while max == 0: 
            nu_max = input('Please enter the maximum range for the game: \n')
            max, nu_max = is_number(nu_max)
        
        if nu_min >= nu_max:
            print(f'The minimum range: {nu_min} is greater than the maximum range: {nu_max}. Please try again.\n')

        else:
            while usr_num == 0: 
                user_number = input('Choose your number for the game: \n')
                usr_num, user_number = is_number(user_number)
            break    
    return nu_min, nu_max, user_number

def to_continiue():    
    while True:
        user_input = input('Play again - Y/N: \n').strip().lower()
        if user_input in ['y', 'n']:
            break
        print('Please enter (Y)es or (N)o.')

    if user_input == 'y':
        return 'y'
    else:
        return 'n'

def the_game():
    start = 'y'
    while start == 'y':
        print('<-- The GAME -->')
        nu_min, nu_max, user_number = user_numbers()
    
        if draw(nu_min,nu_max) == user_number:
            print(f'Congratulations, you WON! The lucky number was {user_number}.')
        else:
            print('Sorry, you LOST this time.')
        time.sleep(1)
        start = to_continiue()

stop = 0
print('-' * 60)
the_game()
print('<-- Game Over. Thanks for playing! -->')