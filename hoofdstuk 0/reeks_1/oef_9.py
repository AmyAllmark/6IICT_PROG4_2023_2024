def letter_checker(woord, letter):
    "return of het woord de letter bevat"
    if letter in woord:
        return True
    else:
        return False 

print( letter_checker("hallo", "e") ) # False
print( letter_checker("dag", "a")   ) # True
