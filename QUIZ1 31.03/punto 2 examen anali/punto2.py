"""Escribir una función recursiva que  encuentre el menor elemento de una lista"""

def menor_elemento(lista,numero_menor):
    if lista == []:
        return  numero_menor
    else:
        numero_actual = lista.pop()
        if numero_actual < numero_menor:
           numero_menor = numero_actual
           return menor_elemento(lista,numero_menor)
        else:
           return menor_elemento(lista,numero_menor)  



l= [1,3,-6,0,]
numero_menor =l[-1]
print("el numero menor de la lista es :",menor_elemento(l,numero_menor))