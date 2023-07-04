
def __binarySearchRec__(n,elements,i,j):

    m = (i + j) // 2

    if i > j:
        return -1
    elif elements[m] == n:
        return m
    elif elements[m] < n:
        return __binarySearchRec__(n, elements, m+1, j)
    else:
        return __binarySearchRec__(n, elements, i, m-1)



def binarySearch(n,elements):
    return __binarySearchRec__(n,elements,0,len(elements)-1)



if __name__ == '__main__':

    N = int(input().strip())

    letras = []
    repeticiones = []

    for _ in range(N):
        var = input()
        C = [w for w in var]
        for l in C:
            if l not in letras:
                letras.append(l)
                repeticiones.append(1)
            else:
                letras.sort()
                index = binarySearch(l,letras)
                if index != -1:
                    repeticiones[index] += 1
        print(letras)
        print(repeticiones)

    best = -1
    sol = -1
    for i in range(len(letras)):
        if best < repeticiones[i]:
            sol = i
            best = repeticiones[i]

    print(letras[sol])