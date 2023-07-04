
def bestItem(repeticiones,letras):
    best = -1
    bestItem = -1

    for i in range(len(letras)):
        if repeticiones[i] > best:
            best = repeticiones[i]
            bestItem = i
    return letras[bestItem]


if __name__ == '__main__':

    N = int(input().strip())

    letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    repeticiones = [0] * len(letras)

    for _ in range(N):
        var = input()
        C = [w for w in var]
        for mayus in C:
            cont = 0
            for l in letras:
                if l == mayus:
                    repeticiones[cont] += 1
                cont += 1
    print(bestItem(repeticiones,letras))
