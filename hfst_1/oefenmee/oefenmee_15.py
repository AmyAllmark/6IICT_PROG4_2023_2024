# Maak voor deze oefen mee gebruik van onderstaande dictionary van dictionaries.
grootste_steden = {
    'Frankrijk': {
        'Parijs': 2140526,
        'Marseille': 869815,
    },
    'Belgie?': {
        'Brussel': 1209000,
        'Antwerpen': 523248,
    },
    'Duitsland': {
        'Berlijn': 3769495,
        'Hamburg': 1841179,
    }
}

for land,steden in grootste_steden.items():# items overloopt het element nog eens je kunt nu zrlfs de waarde van ieder element bepaalen 
    print(f'De grootste steden in {land} zijn:')
    for stad, aantal in steden.items():
        print(stad,aantal)