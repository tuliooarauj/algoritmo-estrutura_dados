def encontra_paredes_adj(celula, tam_labirinto, paredes_internas):
    skip_paredes = tam_labirinto + (tam_labirinto - 1)
    #Abaixo
    
    parede_abaixo = celula + skip_paredes - 1
   
    #Acima
    parede_acima = celula 

    #Direita

    #Esquerda


def main():
    n_labirintos = int(input())

    for i in range(n_labirintos):    
        nmq = input().split()
        tam_labirinto = int(nmq[0])
        qtd_paredes_int_rem = int(nmq[1])
        qtd_consultas = int(nmq[2])

        qtd_paredes_int = 2*(tam_labirinto^2-tam_labirinto)
        paredes_internas = [1] * qtd_paredes_int
        celulas = [] * tam_labirinto^2

        for j in range(qtd_paredes_int_rem):
            parede_removida = int(input())
            paredes_internas[parede_removida] = 0


        for k in range(qtd_consultas):
            consulta = input().split()
            origem = int(consulta[0])
            destino = int(consulta[1])

        



if __name__ == "__main__":
    main()

