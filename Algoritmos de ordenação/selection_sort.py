lista = [7,5,1,8,3]

def selection_sort(lista):
    n = len(lista)
    for j in range(n-1):
        min_idx = j
        for i in range(j, n): #Encontrar o menor
            if lista[i] < lista[min_idx]:
                min_idx = i
        
        if lista[j] > lista[min_idx]: #Trocar
            aux = lista[j] 
            lista[j] = lista[min_idx]
            lista[min_idx] = aux