

def getBestCand(visited,candidates):
    index = -1
    cost = 0x3f3f3f
    for i in range(len(visited)):
        if not visited[i] and candidates[i] < cost:
            cost = candidates[i]
            index = i

    return index


def dikjstra(g,tipo,St):
    n = len(g)
    visited = [False] * n
    candidates = [float('inf')] * n
    roads = [[] for _ in range(n)]
    candidates[St] = 0

    for _ in range(n):
        bestCand = getBestCand(visited,candidates)
        visited[bestCand] = True

        for st,end,w in g[bestCand]:
            if candidates[end] > candidates[st] + w:
                candidates[end] = candidates[st] + w
                if roads[st]:
                    roads[end] = roads[st].copy()
                else:
                    roads[end].append(st)
                roads[end].append(end)

    return roads


if __name__ == '__main__':

    N, M, C = map(int,input().strip().split())

    g = [[] for _ in range(N)]
    tipo = ['x'] * N

    for _ in range(M):
        a,b,w = map(int,input().strip().split())
        g[a].append((a,b,w))
        g[b].append((b,a,w))

    for _ in range(N):
        id,t = input().strip().split()
        tipo[int(id)] = t

    for _ in range(C):
        St, End, r = input().strip().split()
        recorrido = []
        for letra in r:
            recorrido.append(letra)

        indexs = dikjstra(g,tipo,int(St))#[int(End)]

        sol = []
        for i in indexs:
            sol.append(tipo[i])
        print("_______________")
        print(sol)
        print(recorrido)