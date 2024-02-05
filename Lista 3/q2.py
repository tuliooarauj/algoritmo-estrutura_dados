def parent(idx):
    return idx // 2

def left(idx):
    return (idx * 2) + 1

def right(idx):
    return (idx * 2) + 2 

def len_heap(array):
    n = 0
    for _ in array:
        n += 1
    return n

def switch(array, elem1, elem2):
    aux = array[elem1]
    array[elem1] = array[elem2]
    array[elem2] = aux

def max_heapify(array, idx, array_size):

    if not idx < 0:
        
        left_idx = left(idx)
        right_idx = right(idx)
        if left_idx <= array_size - 1 and array[left_idx] != None and array[left_idx] > array[idx]:
            
            maior = left_idx
        else:
            maior = idx

        if right_idx <= array_size - 1 and array[right_idx] != None and array[right_idx] > array[maior]:

            maior = right_idx
        
        if maior != idx:
            switch(array, idx, maior)
            max_heapify(array, maior, array_size)

def build_max_heap(array, array_size):
    for idx in range((array_size//2), -1, -1):
        max_heapify(array, idx - 1, array_size)
        
def cria_filas(n_fileiras, n_assentos):
    i = 0
    fileiras = [[]] * n_fileiras
    for fileira in fileiras:
        fileiras[i] = [None] * n_assentos
        i += 1
    return fileiras

def retorna_idx(array, buscado):
    idx = 0
    for element in array:
        if element == buscado:
            return idx
        idx += 1

def encontra_menor(array):
    menor = array[0]
    for element in array:
        if element < menor:
            menor = element
    return menor
        

def insere_na_fila(filas, prioridade, fila_sem_assento):
    n_fileira = 0
    for fila in filas:
        n_assento = 0
        n_fileira += 1
        for assento in fila:
            if assento is None:
                fila[n_assento] = prioridade
                return n_fileira
            n_assento += 1
    
    menor_prioridade = 0
    fila_menor_prioridade = 0

    i = 0
    for fila in filas:
        i+=1 
        heap_size = len_heap(fila)
        build_max_heap(fila, heap_size)
        menor = encontra_menor(fila)
        if i == 1:
            menor_prioridade = menor
        if menor < menor_prioridade:
            fila_menor_prioridade += 1
            menor_prioridade = menor
        
    if prioridade > menor_prioridade:
        idx = retorna_idx(filas[fila_menor_prioridade], menor_prioridade)
        filas[fila_menor_prioridade][idx] = prioridade
        fila_sem_assento += [None]
        j = 0
        for element in fila_sem_assento:
            if element is None:
                fila_sem_assento[j] = menor_prioridade
                heap_size = len_heap(fila_sem_assento)
                build_max_heap(fila_sem_assento, heap_size)
            j += 1
        build_max_heap(filas[fila_menor_prioridade], heap_size)

        return fila_menor_prioridade + 1
    
    return None

def main():
    fileira_assentos = input().split()
    n_fileiras = int(fileira_assentos[0])
    n_assentos = int(fileira_assentos[1])

    qtd_comandos = int(input())

    fila_cadastro = [None]

    filas_assentos = cria_filas(n_fileiras, n_assentos)
    fila_sem_assento = []

    aux = 0
    n_cadastro = 0

    while aux < qtd_comandos:
        aux += 1

        comando_nome_prior = input().split()
        comando = comando_nome_prior[0]
        nome = comando_nome_prior[1]

        if comando == 'CAD':
            prioridade = int(comando_nome_prior[2])
            fila_cadastro += [None]
            for element in fila_cadastro:
                if element is None:
                    n_cadastro += 1
                    fila_cadastro[n_cadastro] = [nome, prioridade]
                    n_fileira = insere_na_fila(filas_assentos, prioridade, fila_sem_assento)
                    if n_fileira:
                        print('{} ({}) foi alocado(a) na fileira {}'.format(nome, n_cadastro, n_fileira))
                    else:
                        print('{} ({}) nao foi alocado(a) em nenhuma fileira'.format(nome, n_cadastro))
            
        elif comando == 'REM':
            encontrou = False
            i = 0
            for _ in fila_cadastro:
                i += 1
                if nome == fila_cadastro[i][0]:
                    n_prioridade_pessoa = fila_cadastro[i][1]
                    encontrou = True
            if encontrou == False:
                print('Inexistente')

            j = 0
            for fila in filas_assentos:
                j += 1
                k = 0
                for num_pessoa in fila:
                    if num_pessoa == n_prioridade_pessoa:
                        print('Removido(a)')
                        filas_assentos[j][k] = fila_sem_assento[0]
                        heap_size = n_assentos
                        build_max_heap(filas_assentos[j], heap_size)
                    k += 1

            l = 0
            for num_pessoa in fila_sem_assento:
                if num_pessoa == n_prioridade_pessoa:
                    print('Removido(a)')
                    fila_sem_assento[l] = None
                l += 1

       
        elif comando == 'VER':
            numero_cadastro = int(comando_nome_prior[2])
            encontrou = False 

            i = 0
            for cadastro in fila_cadastro:
                if cadastro:
                    if nome == cadastro[0] and i == numero_cadastro:
                        n_prioridade_pessoa = cadastro[1]
                        encontrou = True
                i += 1

            if encontrou == False:
                print('Inexistente')

            if encontrou == True:
                presente = False
                j = 0
                for fila in filas_assentos:
                    j += 1
                    for num_pessoa in fila:
                        if num_pessoa == n_prioridade_pessoa:
                            print('Sentado(a) na fileira {}'.format(j))
                            presente = True

                if not presente:
                    for num_pessoa in fila_sem_assento:
                        if num_pessoa == n_prioridade_pessoa:
                            print('Sem assento')

            

if __name__ == '__main__':
    main()





