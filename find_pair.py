# MÃ©dicoSoft 2020
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

def find_pair2(array, sum) -> [1,2]:
    hashset = set()
    for num in array:
        hashset.add(num)
    for num in array:
        if sum-num in hashset:
            return [num,sum-num]
    return [0,0]

print(find_pair2([1,3,4,5,6],123))
print(find_pair2([1,3,4,5,6],11))

# El orden es nlogn de find_pair
# El orden es n , podría decirse que 2 n para find_pair2, pero por que use el hashset, sería interesante la cantidad de memoria.