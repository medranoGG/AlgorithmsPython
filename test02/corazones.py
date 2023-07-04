from collections import deque


def bfs(g,St,End,recorrido,tipo):
    n = len(g)
    visited = [False] * n
    sol = []
    isSol = False
    cont = 1

    q = deque()
    q.append(St)
    visited[St] = True
    sol.append(St)

    while q and not isSol:
        aux = q.popleft()
        for adj in g[aux]:
            if not  visited[adj] and cont < len(recorrido) and tipo[adj] == recorrido[cont]:
                q.append(adj)
                visited[adj] = True
                cont += 1
                sol.append(adj)
                if adj == End:
                    return sol

    return False



if __name__ == '__main__':

    N, M, C = map(int,input().strip().split())

    g = [[] for _ in range(N)]
    tipo = ['x'] * N

    for _ in range(M):
        a,b,w = map(int,input().strip().split())
        g[a].append(b)
        g[b].append(a)

    for _ in range(N):
        id,t = input().strip().split()
        tipo[int(id)] = t

    for _ in range(C):
        St, End, r = input().strip().split()
        recorrido = []
        for letra in r:
            recorrido.append(letra)

        sol = bfs(g,int(St),int(End),recorrido,tipo)
        if sol:
            print(*sol)
        else:
            print('No se puede llegar')
