# MédicoSoft 2020
# 1. Encuentra el par con la suma dada en el arreglo
# Lee el README.md antes de comenzar
def find_pair(array, sum) -> [1, 2]:
    """Arguents:
        array -- unsorter array of integers
        sum -- sum of pair of integers to find
    Retorna:
        array -- array of two elements with the integers of sum to find
    """
    #O(n^2)
    i = 0
    stop_loops = True
    result = []
    while i < len(array) - 1 and stop_loops == True:
        j = i + 1
        while j < len(array) and stop_loops== True:
            new_sum = array[i] + array[j]
            if new_sum == sum:
                result.append(array[i])
                result.append(array[j])
                stop_loops = False
            j += 1
        i += 1
    return result
    
