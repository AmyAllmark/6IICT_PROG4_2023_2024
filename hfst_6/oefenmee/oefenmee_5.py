
# examen 

# code voor somatie van elk getal


# Niveau 1: bepaal sommatie van een getal recursief.
n= int(input("geef een getal in: "))

# somatie 5 = 5 + somatie 4
#somatie n = n + somatie(n-1)
""" Geraamte van de functie. """
def sommatie(n):
    if n == 1:
        return 1
    return n + sommatie(n-1)

""" Geeft faculteit van 1 terug. """
print( sommatie(n) )   # 1


# Niveau 2: bepaal sommatie van een getal met while-loop.



# print( sommatie(1) )   # 1
# print( sommatie(2) )   # 3
# print( sommatie(3) )   # 6
# print( sommatie(4) )   # 10
# print( sommatie(5) )   # 15
# print( sommatie(100) ) # 5050
