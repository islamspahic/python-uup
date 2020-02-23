def Kvadar(visina, sirina, duzina):
    return {
        'visina' : visina
        'sirina' : sirina
        'duzina' : duzina
     }

def proveraKvadra(kvadar):
    potrebnaPolja = ['visina', 'sirina', 'duzina']
    for polje in potrebnaPolja:
        if polje not in kavadar.keys():
            print('Kvadar mora da ima kljuc ' + polje)
            return 0
    return 1

def zapremina(kvadar):
    if proveraKvadra(kvadar) == 0:
        return 0
    
        return kvadar['visina'] * kvadar['sirina'] * kvadar['duzina']

def povrisina(kvadar):
    if proveraKvadra(kvadar) == 0:
        return 0

    return 2 * (kvadar['sirina'] * kvadar['visina'] +
                kvadar['sirina'] * kvadar['duzina'] +
                kvadar['duzina'] * kvadar['visina'])
