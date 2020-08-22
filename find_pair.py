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
    difference = 0
    position_num2 = 0

    for index, num in enumerate(array):
        difference = sum - num

        try:
            position_num2 = array.index(difference, (index+1), len(array))

            return [num, array[position_num2]]
            break
        except:
            pass

    return [0, 0]


result = find_pair([1, 5, 6, 7, 3, 5], 11)

for num in result:
    print(num, " ")
