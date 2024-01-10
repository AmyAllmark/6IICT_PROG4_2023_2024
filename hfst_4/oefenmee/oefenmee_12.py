def deel(teller, noemer):
    if type(teller) != int:
        raise TypeError( "teller is geen int")

    if type(noemer)!= int:
        raise TypeError( "noemer is geen int")

    if noemer == 0:
        raise ZeroDivisionError("Snul.")
    return teller/noemer

    
print( deel(8, 2) )      # 4.0

#print( deel(9, 0) )      # ZeroDivisionError: Snul.
#print( deel(True, 4) )   # TypeError: True is <class 'bool'>, moet int/float zijn.
print( deel(8, "a")  )   # TypeError: a is <class 'str'>, moet int/float zijn.
print( deel(True, "a") ) # TypeError: True is <class 'bool'>, moet int/float zijn.
