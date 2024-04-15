# examen 


# Draai een woord om.

def draaiom(woord):
    if len(woord) ==1:
        return woord
    
    draaiom_woord = woord[-1]+ draaiom(woord[0:-1]) #hij kijkt naar het woord bv hallo en doet min 1 dus je hebt dan hall ([0:-1])
    return draaiom_woord

print( draaiom("Hallo") )       # ollaH
print( draaiom("Dag") )         # gaD
print( draaiom("f"))            # f
print( draaiom("Iedereen") )    # neeredeI
