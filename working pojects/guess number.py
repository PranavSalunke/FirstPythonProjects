## guess random number game## 

# all the imports!!
import random
import time


#game code
def guess_game():
    """
    This is the guessing game. n is the value to geuss from. 1 -> n   
    """
    
    x = 1
    tries=1
    n = int(raw_input('what is the number you want to guess from? (values go from 1 --> n)\n'))
    num2guess = random.randint(1,n)
    print ('.\n')
    time.sleep(.25),
    print('..\n')
    time.sleep(.3),
    print ('...\n')
    time.sleep(.5),
    print ('my number is between 1 and %s') % n
    num_guessed = raw_input('now your turn to GUESS! What is your guess?\n')
    while x == 1:
        if int(num_guessed) == int(num2guess):
            print 'thats RIGHT!\nyou did that in %s attempt(s)' %tries
            x = 2
            time.sleep(1)
            # to keep the program running
            isthethingrunning = raw_input( )
        else:
            print '\nthat\'s not right'
            if int(num_guessed) > int(num2guess):
                print ('your guess is too HIGH!')
            if int(num_guessed) < int(num2guess):
                print('your guess is too LOW')
            num_guessed = raw_input('guess again:\n')
            tries +=1  
#run game
guess_game()

## to keep the program running
print '\n\n'
is_the_thing_running = raw_input('press enter to exit..' )