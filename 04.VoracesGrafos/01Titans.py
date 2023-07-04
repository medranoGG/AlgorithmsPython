from random import randint

def getBestNode(candidates,visited):
    cost = 0x3f3f3f
    bestNode = -1

    for i in range(len(visited)):
        if not  visited[i] and candidates[i] < cost:
            cost = candidates[i]
            bestNode = i

    return bestNode, cost


def emt(g):
    n = len(g)
    visited = [False] * n
    candidates = [float('inf')] * n
    sol = 0

    init = randint(0,n-1)
    visited[init] = True
    for st,end,w in g[init]:
        candidates[end] = w

    for i in range(n-1):
        bestNode, cost = getBestNode(candidates,visited)

        if cost < float('inf'):
            sol += cost
            visited[bestNode] = True
        for st,end,w in g[bestNode]:
            if not visited[end]:
                candidates[end] = min(candidates[end],w)

    if sol % 5 == 0:
        return sol//5
    else:
        return sol//5 + 1


if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    g = [[] for i in range(N)]

    for _ in range(M):
        a, b, w = map(int,input().strip().split())
        g[a].append((a,b,w))
        g[b].append((b,a,w))

    print(emt(g))