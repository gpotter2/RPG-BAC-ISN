# -*- coding: utf-8 -*-

import json

def charger_fichier(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        data = json.load(fichier)
    return data

def ecrire_fichier(chemin_fichier, data):
    with open(chemin_fichier, 'w') as fichier:
        fichier.write(json.dumps(data))

"""
Exemples:

ECRIRE:

data = {"a": "bonjour",
        "b": "au revoir",
        "c": 12}
ecrire_fichier("data.json", data)

LIRE:

data = charger_fichier("data.json")

==> {'a': 'bonjour', 'b': 'au revoir', 'c': 12}

"""
