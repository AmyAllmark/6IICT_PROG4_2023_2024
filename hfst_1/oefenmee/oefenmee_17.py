# Maak voor deze oefen mee gebruik van onderstaande dictionary-structuur.
inception_film = {
    'jaar': 2010,
    'genre': ['Actie', 'Sciencefiction', 'Thriller'],
    'cast': [ 
        {'acteur': 'Leonardo DiCaprio', 'rol': 'Cobb'},
        {'acteur': 'Joseph Gordon-Levitt', 'rol': 'Arthur'},
        {'acteur': 'Ellen Page', 'rol': 'Ariadne'}
    ],
    'locaties': ['Parijs', 'Los Angeles', 'Tokio'],
    'box_office': {'budget': 160000000, 'opbrengst': 829895144},
    'awards': {'Oscars': 0, 'Golden Globes': 4}
}
print(f'het jaar dat de film uitkwam: {inception_film["jaar"]}')
print(inception_film["genre"][1])
print((f'opbrengst van de film: { inception_film["box_office"]["opbrengst"]}'))
print(f' De rol van acteur Leonardo DiCaprio: {inception_film["cast"][0]["rol"]}')
inception_film['awards']['Oscars']=4
print(inception_film['awards']['Oscars'])
inception_film['regisseur']='Christopher Nolan'
inception_film['cast'][2]['acteur']=' Tom Hardy'

print(inception_film)
