

def esFactible(grafo, sol, nodo, color):
    fact = True
    i = 0
    ady = grafo[nodo]
    while fact and i < len(ady):
        if sol[ady[i]] != 0: #ady[i] < nodo: #
            fact = color != sol[ady[i]]
        i += 1
    return fact


def coloreadoVA(g, m, sol, nodo):
    if nodo == len(g):
        esSol = True
    else:
        esSol = False
        color = 1
        while not esSol and color <= m:
            if esFactible(g, sol, nodo, color):
                sol[nodo] = color
                esSol, sol = coloreadoVA(g, m, sol, nodo+1)
                if not esSol:
                    sol[nodo] = 0
            color += 1
    return esSol, sol


if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    g =[[] for _ in range(N)]
    sol = [0] * N

    for _ in range(M):
        a,b = map(int,input().strip().split())
        g[a].append(b)
        g[b].append(a)

    m = 3
    nodo = 0
    esSol, sol = coloreadoVA(g, m, sol, nodo)

    if esSol:
        print(sol)
    else:
        print("No se encuentra solucion")
