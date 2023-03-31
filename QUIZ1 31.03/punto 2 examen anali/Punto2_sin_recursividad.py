lista=[5,2,0,2,3,-3]         #O(1)

numero_menor = lista(0)  #O(1)
 

for i in lista:            #O(n)
    if numero_menor > i:   #O(1)
        numero_menor = i   #O(1)

print("el numero menor de la lista,",lista," es: ",numero_menor)

"""O(1)+O(1)+O(1)+O(1)+O(n)= O(n) """
""" la complejidad del algoritmo es: O(n)"""