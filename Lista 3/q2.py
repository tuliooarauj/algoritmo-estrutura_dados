# 1 - Montar a estrutura do min-heap para determinar as prioridades da fila
# 2 - Montar a estrutura da tabela hash para alocar as pessoas nos assentos e as que estão fora

# Filas de assentos
# Fila de pessoas sem assentos
# Fila de cadastro

def main():
    fileira_assentos = input().split()
    n_fileiras = int(fileira_assentos[0])
    n_assentos = int(fileira_assentos[1])

    qtd_comandos = int(input())

    fila_cadastro = [None]

    i = 0
    j = 0

    while i < qtd_comandos:
        i += 1

        comando_nome_prior = input().split()
        comando = comando_nome_prior[0]
        nome = comando_nome_prior[1]

        if comando == 'CAD':
            prioridade = comando_nome_prior[2]
            fila_cadastro += [None]
            for element in fila_cadastro:
                if element is None:
                    fila_cadastro[j] = nome
                j += 1

        elif comando == 'REM':
            pass

        elif comando == 'VER':
            pass

if __name__ == '__main__':
    main()