import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def getSecretNum():
    """Returns a string made of NUM_DIGITS unique random digits."""
    numbers = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)   # shuffling the numbers randomly
    # now we take the first NUM_DIGITS numbers from the list and make a string
    secretNumbers = ""
    for i in range(NUM_DIGITS):
        secretNumbers += numbers[i]
    # then just return the secretString
    return secretNumbers
