# MédicoSoft 2020
# 1. Encuentra el par con la suma dada en el arreglo
# Lee el README.md antes de comenzar


def find_pair(array, sum):
    for i in range (0, len(array), 1):
        z = array [i]
        for j in range (i+1, len(array), 1):
            y = array [j]
            if z + y == sum:
                print (z, y)
       # array [i] = None   
            
            

def envio_variables():
    array = [2,4,0,6,1,7,8,3,2,5,25]
    sum = 3
    find_pair(array, sum)

envio_variables()