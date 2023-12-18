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

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

def merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if fim - inicio > 1: #Caso base
        meio = (fim + inicio) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    return lista

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left = 0
    top_right = 0
    for k in range(inicio, fim):
        '''Caso onde a sublista da esquerda é toda menor que a sublista da direita, 
        dessa forma é preciso verificar se ainda há elementos a ser comparados já que toda vez o topo
        é incrementado.
        '''    
        if top_left >= len(left): 
            lista[k] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left += 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left += 1
        else:
            lista[k] = right[top_right]
            top_right += 1

def quick_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        pivot = partition(lista, inicio, fim)
        quick_sort(lista, inicio, pivot - 1)
        quick_sort(lista, pivot + 1, fim)
    return lista

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            aux = lista[j] 
            lista[j] = lista[i]
            lista[i] = aux
        i += 1
    aux2 = lista[i]
    lista[i] = lista[fim]
    lista[fim] = aux2
    return i

print(bubble_sort(lista))
print(selection_sort(lista))
print(insertion_sort(lista))
print(merge_sort(lista))
print(quick_sort(lista))