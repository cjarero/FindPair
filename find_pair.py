# MédicoSoft 2020
# 1. Encuentra el par con la suma dada en el arreglo
# Lee el README.md antes de comenzar

def find_pair(array, sum) -> [1,2]:
    """Arguents:
        array -- unsorter array of integers
        sum -- sum of pair of integers to find
    Retorna:
        array -- array of two elements with the integers of sum to find
    """

     #O(n2)

    array_result = []
    for i in range(len(array)):
        for j in range(len(array)):
                if (array[i] + array[j]) == sum and i!=j:
                    array_result = [array[i], array[j]]
    return array_result