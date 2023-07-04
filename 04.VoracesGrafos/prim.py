from random import randint


def getBestNode(candidates,visited):
    bestCost = 0x3f3f3f
    bestItem = -1

    for i in range(len(visited)):
        if not visited[i] and candidates[i] < bestCost:
            bestCost = candidates[i]
            bestItem = i

    return bestItem, bestCost


def prim(g):
    n = len(g)
    visited = [False] * n
    candidates = [float('inf')] * n
    sol = 0 ##

    init = randint(0,len(g)-1)
    visited[init] = True
    for st, end, w in g[init]:
        candidates[end] = w

    for _ in range(n-1):
        bestNode, cost = getBestNode(candidates, visited)
        visited[bestNode] = True
        sol += cost ##

        for st, end, w in g[bestNode]:
            if not visited[end]: ## Porque solo quuero veros una vez y ya
                candidates[end] = min(candidates[end],w)

    return sol



if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    g = [[] for i in range(N)]

    for i in range(M):
        a, b, w = map(int,input().strip().split())
        g[a].append((a,b,w))
        g[b].append((b,a,w))

    print(prim(g))
