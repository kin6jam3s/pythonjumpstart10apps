import random

print('--------------------------')
print(' GUESS THAT NUMBER GAME')
print('--------------------------')
print()

# Select random number from 0 - 100
the_number = random.randint(0, 10)

#   guess_text = input('Guess a number between 0 and 100: ')
#    # Convert guest_text to int
#    guess = int(guess_text)

# This is the initial value of guess - needs to be defined to avoid error
guess = -1  # should be a non winning guess!
name = input('Enter your name: ')

# This will make a loop while guess is NOT equal to the random number
while guess != the_number:
    # Inserted user input under while condition to void loop
    guess_text = input('Guess a number between 0 and 10: ')
    # Convert guest_text to int
    guess = int(guess_text)

    # Conditional statement
    if guess < the_number:
        print('Sorry {} Your guess of {} is too low'.format(name, guess))
    elif guess > the_number:
        print('Sorry {} Your guess of {} is too high'.format(name, guess))
    else:
        print('Excellent work {} Your guess of {} is correct!'.format(name, guess))

print('Done')
