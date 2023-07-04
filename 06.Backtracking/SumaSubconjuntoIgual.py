def sumarValores(conj, ind):
    izq = conj[0]
    der = 0
    for i in range(ind):
        izq += conj[i]
        print("izq", izq)
    for j in range(ind+1, len(conj)):
        der += conj[j]
        print("der", izq)
    return der, izq

def esSolucion(conj, ind, tupla):
    if ind < len(tupla):
        return False
    else:
        suma = 0
        for i in range(len(tupla)):
            suma += tupla[i]*conj[i]
        return suma == 0

def sumaVA(conj, ind, tupla):
    if esSolucion(conj, ind, tupla):
        esSol = True
    else:
        esSol = False
        if ind < len(tupla):
            tupla[ind] = -1
            esSol, tupla = sumaVA(conj, ind+1, tupla)
            if not esSol:
                tupla[ind] = 1
                esSol, tupla = sumaVA(conj, ind+1, tupla)
                if not esSol:
                    tupla[ind] = 0
    return esSol, tupla

def imprimirSol(tupla,conjunto):
    print('Conjunto -1:',end='')
    for i in range(len(tupla)):
        if tupla[i] == -1:
            print(conjunto[i],end=' ')
    print()
    print('Conjunto 1:', end='')
    for i in range(len(tupla)):
        if tupla[i] == 1:
            print(conjunto[i], end=' ')
    print()

#11.- Dado un conjunto de n enteros, necesitamos decidir si puede ser descompuesto en dos
#subconjuntos disjuntos cuyos elementos sumen la misma cantidad.
#PROGRAMA PRINCIPAL
conjunto = [7, 2, 3, 4, 8]
indiceActual = 0
tupla = [0] * len(conjunto)
esSol, tupla = sumaVA(conjunto, indiceActual, tupla)
if esSol:
    print('Se ha encontrado una solución y es:')
    imprimirSol(tupla,conjunto)
else:
    print('No se ha encontrado una solución')
