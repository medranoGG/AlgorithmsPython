import math


def getBestCand(benef,pesos,candidates):
    bestRatio = -1
    idx = -1

    for c in candidates:
        ratio = benef[c] / pesos[c]
        if ratio > bestRatio:
            bestRatio = ratio
            idx = c

    return idx


def knapsack(benef,pesos,max_peso,fichados):
    n = len(pesos)
    candidates = set(range(n))
    sol = [-1] * n
    isSol = False

    while not isSol and candidates:
        besCand = getBestCand(benef,pesos,candidates)
        candidates.remove(besCand)
        if not fichados[besCand]:
            if pesos[besCand] <= max_peso:
                sol[besCand] = 1
                max_peso -= pesos[besCand]
                fichados[besCand] = 1
            else:
                sol[besCand] = max_peso / pesos[besCand]
                isSol = True
                fichados[besCand] = 1

    return sol


if __name__ == '__main__':

    N, M, C = map(int,input().strip().split())
    presis = []
    jugadores = []
    beneficio = []
    pesos = []
    fichados = [0] * M

    for _ in range(N):
        presis.append(input().strip())
        pesos.append([])

    for _ in range(M):
        datos_jugador = list(input().strip().split())
        name = datos_jugador[0]
        benef = datos_jugador[1]
        jugadores.append(name)
        beneficio.append(int(benef))
        datos_jugador.remove(benef)
        datos_jugador.remove(name)

        for i in range(N):
            p = datos_jugador[0]
            pesos[i].append(int(p))
            datos_jugador.remove(p)

    for i in range(N):
        print(presis[i],end=":")
        sol = knapsack(pesos[i],beneficio,C,fichados)
        cont = 0
        fin = []
        for j in range(len(sol)):
            if sol[j] != -1:
                cont += sol[j] * pesos[i][j]
                fin.append(jugadores[j])
        print(math.ceil(cont))
        fin.sort()
        for f in fin:
            print(f)


