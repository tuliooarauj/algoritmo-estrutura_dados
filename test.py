def encontra_menor(array):
    menor = array[0]
    for element in array:
        if element < menor:
            menor = element
    
    return menor

print(encontra_menor([1,2,3,4,5,1,231,321,312,1,0,-20]))