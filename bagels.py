import random

print(__name__)

NUM_DIGITS = 3
MAX_GUESSES = 10

def getSecretNum():
    """Returns a string made of NUM_DIGITS unique random digits."""
    numbers = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)   # shuffling the numbers randomly
    # now we take the first 3 NUM_DIGITS numbers from the list and make a string
    secretNumbers = ""
    for i in range(NUM_DIGITS):
        secretNumbers += str(numbers[i])
    # then just return the secretString
    return secretNumbers



def getClues(guess,SecretNum):
    
    """Returns a string with the pico, fermi, bagels clues for a guess
     and secret number pair."""
    
    if guess==SecretNum:
     return 'You got it!'
    clues=[]
    for i in range(len(guess)):
      if guess[i]==SecretNum[i]:
        clues.append(' Fermi ') #Correct digit in the correct place
      elif guess[i] in SecretNum:
        clues.append(' Pico ') # Correct digit in incorrect place
    if len(clues)==0:
     return 'Bagels' #Incorrect digits
    #Sort the clues into alphabetical order so their original order so it doesn't give information away.
    else:
     clues.sort()
    # Make a single string from the list of string clues.
     return ''.join(clues)


# the main game loop.
def main():
    # print an intro message
    print(f'''Bagels, a deductive logic game.
    
I am thinking of a {NUM_DIGITS} digit number with no repeated digits. Try to guess what it is.
Here are some clues:

when I say              what that means
Pico                    one digit is correct but in the wrong position.
Fermi                   one digit is correct and it's in the correct position.
Bagels                  no digit is correct.''')

    while True:
        secretNum = getSecretNum()  # this stores the secret number
        print("I've thought up a number.")
        print(f"You have {MAX_GUESSES} guesses to get it.")
        # now let's do the guess-check-feedback loop
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal:
                print(f"Guess #{numGuesses}: ")
                guess = input("> ")
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # They're correct. so  brek out of this loop.
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secretNum}.")  
                # we don't need to break here 'cause the loop will end by itself.
        # ask the player if they want to play again
        print('Do you want to play again? (yes or no)') 
        if not input('> ').lower().startswith('y'):
            break
    print("Thanks for playing!")

# finally, let's start the game loop if the program is run (not imported)
if __name__ == "__main__":
    # __name__ is a built-in variable. it's always defined in all python scripts.
    # its value will be "__main__" if the script is run
    # its value will be the name of the script file if the script is imported.
    main()