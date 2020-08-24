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

    #Se utiliza O(AB).
    i = 0
    while i<len(array):

        for j in range(len(array)):
            if array[i] + array[j] == sum:
                array_result=[array[i],array[j]]
                i= len(array)
                break
        i+=1
        
    return array_result

c= find_pair([4,6,9,15,73,5],88)
print (c)