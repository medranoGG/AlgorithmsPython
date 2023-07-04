


def getBestNode(candidates,visited):
    bestCost = 0x3f3f3f
    bestItem = -1

    for i in range(len(visited)):
        if not visited[i] and candidates[i] < bestCost:
            bestCost = candidates[i]
            bestItem = i

    return bestItem


def dijkstra(g):
    n = len(g)
    visited = [False] * n
    candidates = [float('inf')] * n  # Candidates = sol

    init = 0
    visited[init] = True
    candidates[init] = 0 ##
    for st, end, w in g[init]:
        candidates[end] = w

    for i in range(n-1):
        bestNode = getBestNode(candidates, visited)
        visited[bestNode] = True

        for st, end, w in g[bestNode]:
            candidates[end] = min(candidates[end], candidates[st] + w)

    return candidates


if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    g = [[] for i in range(N)]

    for i in range(M):
        a, b, w = map(int,input().strip().split())
        g[a].append((a,b,w))
        g[b].append((b,a,w))

    print(dijkstra(g))
