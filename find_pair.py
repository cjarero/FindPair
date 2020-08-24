# MédicoSoft 2020
# 1. Encuentra el par con la suma dada en el arreglo
# Lee el README.md antes de comenzar

def find_pair(array, sum) -> [1,2]:
    resultado = [0,0]
    array.sort()
    minimo = 0
    maximo = len(array)-1
    while minimo < maximo:
        suma = array[minimo]+array[maximo]
        if suma == sum:
            resultado[0] = array[minimo]
            resultado[1] = array[maximo]
            return resultado
        if suma < sum:
            minimo = minimo+1
        else:
            maximo = maximo-1
    return resultado
    """Arguents:
        array -- unsorter array of integers
        sum -- sum of pair of integers to find
    Retorna:
        array -- array of two elements with the integers of sum to find
    """
    
#print(find_pair([1,3,4,5,6],11))
#print(find_pair([1,3,4,5,6],11))

# El orden es nlogn