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
    return lista
        
def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                aux = lista[i] 
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
    return lista

print(bubble_sort(lista))
print(selection_sort(lista))