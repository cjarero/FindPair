"""# MedicoSoft 2020
# 1. Encuentra el par con la suma dada en el arreglo
# Lee el README.md antes de comenzar

# def find_pair(array, sum) -> [1,2]:
Arguents:
        array -- unsorter array of integers
        sum -- sum of pair of integers to find
    Retorna:
        array -- array of two elements with the integers of sum to find
    """
# Input
array = [1,5,6,7,3,5]
sum = 10
# Output
#[7,3] or [5,5]

def findPair(newArray,sum):
    #clonamos nuestra lista para no afectar a la lista original
    array = newArray[:] 
    for item in newArray:         
        #restamos el elemento actual al parametro suma
        res = sum - item
        #Ahora buscamos si el resultado de la resta existe en la lista
        if res in array:           
            #Si existe entonces cremos una lista nueva
            LIST = []
            #obtenemos el indice que le corresponde al valor de la resta
            position = array.index(res)
            #agregamos a la lista nueva el item y su compelmento para formar la suma
            LIST.append(item)
            LIST.append(array[position])                       
            #imprimimos la nueva lista
            print(LIST)
            #eliminamos el item y su complemento para no duplicar busquedas
            array.pop(array.index(item))
            array.pop(position)
        
           
       

findPair(array,sum)

"""
Big O notation

este algortimo cuenta con una O(n) (complejidad Lineal) ya que su nivel de complejidad se basa en dar
una recorrido completo solo una ves a lista que se le proporciona, y realizando las mismas operaciones solo una ves durante cada iteracion
"""
