def ordina(lista):
    '''
    ordinare gli elementi con il seguente algoritmo: 
    Ad esempio ricevo la lista **[2 3 1]** 
    Trovo l'elemento minimo e scambio l'elemento minimo con il primo 
    (scambio 1 e 2) **[1 3 2]** 
    Ripeto l'operazione saltando il primo elemento 
    (che è già ordinato). 
    Trovo il minimo tra **[3 2]** cioè 2 e scambio **[1 2 3]**
    '''
    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista
