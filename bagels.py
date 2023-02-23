import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def getSecretNum():
    """Returns a string made of NUM_DIGITS unique random digits."""
    numbers = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)   # shuffling the numbers randomly
    # now we take the first 3 NUM_DIGITS numbers from the list and make a string
    secretNumbers = ""
    for i in range(NUM_DIGITS):
        secretNumbers += numbers[i]
    # then just return the secretString
    return secretNumbers

secretNumber=getSecretNum()
clues=[]
def getClues(guess,SecretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
     and secret number pair."""
    if guess==SecretNum:
     return 'You got it!'
    for i in range(len(guess)):
      if guess[i]==SecretNum[i]:
        clues.append('Fermi') #Correct digit in the correct place
      elif guess[i] in SecretNum:
        clues.append('Pico') # Correct digit in incorrect place
    if len(clues)==0:
     clues.append('Bagels') #Incorrect digits
    #Sort the clues into alphabetical order so their original order so it doesn't give information away.
    clues.sort()
    # Make a single string from the list of string clues.
    return ''.join(clues)

    
        


