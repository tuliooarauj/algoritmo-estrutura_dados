cont_instrucao = 0 #contador

i = 2
cont_instrucao += 1

ehPrimo = True
cont_instrucao += 1

numero = 5 # nao conta pq eh a entrada

while i < numero:
    cont_instrucao += 1
    
    if numero % i == 0:
        cont_instrucao += 1
        ehPrimo = False
        cont_instrucao += 1
    else:
        cont_instrucao += 1 #caso nao entre no if

    i += 1
    cont_instrucao += 1

else:
    cont_instrucao += 1 #caso nao entre no while

if ehPrimo and numero != 1:
    cont_instrucao += 1
    print(numero, "eh primo")
    cont_instrucao += 1
else:
    cont_instrucao += 1
    print(numero, "nao eh primo")
    cont_instrucao += 1

print(f'Número de instruções: {cont_instrucao}')