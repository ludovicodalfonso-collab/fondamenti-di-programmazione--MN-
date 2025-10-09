def leggi_numero():
    return int(input("Inserisci un numero: "))

def lista_numeri(n):
    '''
    leggi una lista di n numeri
    '''

    lista = []
    for _ in range(n):
        lista.append(leggi_numero())
    return lista

def somma_numeri(lista):
    return sum(lista)

def media_numeri(lista):
    '''
    calcola la media dei numeri nella lista
    '''
    if len(lista) == 0:
        return 0
    return somma_numeri(lista) / len(lista)

def deviazione_standard(lista):
    '''
    calcola la deviazione standard dei numeri nella lista.
    '''
    m = media_numeri(lista)
    sq = []
    for x in lista:
        sq.append((x - m) ** 2)
    
    var = media_numeri(sq)
    return var ** 0.5
    


n = leggi_numero()
lista = lista_numeri(n)
media = media_numeri(lista)
print(media)
deviazione = deviazione_standard(lista)
print(deviazione)