# Maak voor deze oefen mee gebruik van onderstaande dictionary van dictionaries.
spelinfo = {
    'speler1': {
        'naam': 'Alice',
        'positie': {
            'x': 10,
            'y': 5
        },
        'inventaris': {
            'wapen': 'zwaard',
            'goud': 50
        }
    },
    'speler2': {
        'naam': 'Bob',
        'positie': {
            'x': 2,
            'y': 8
        },
        'inventaris': {
            'wapen': 'boog',
            'goud': 9999999999
        }
    }
}
print(f'naam van spreler2: {spelinfo["speler2"]["naam"]}')

#De positie van speler1: {'x':10, 'y':5} 

print(f'positie speler1: {spelinfo["speler1"]["positie"]}')
#Het wapen van speler2: Boog
print(f'wapen speler2: {spelinfo["speler2"]["inventaris"]["wapen"]}')

#speler2 goud waarde naar 0 zetten 
spelinfo["speler2"]["inventaris"]["goud"]=0

spelinfo['speler1']["inventaris"]["bepantsering"]= "schild"

print(spelinfo)