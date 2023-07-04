
def getBestNode(candidates,visited):
    cost = 0x3f3f3f
    bestNode = -1

    for i in range(len(visited)):
        if not visited[i] and candidates[i] < cost:
            cost = candidates[i]
            bestNode = i

    return bestNode


def boom(g,init):
    n = len(g)
    visited = [False] * n
    candidates = [float('inf')] * n

    visited[init] = True
    candidates[init] = 0
    for st,end,w in g[init]:
        candidates[end] = w

    for _ in range(n-1):
        bestNode = getBestNode(candidates,visited)
        visited[bestNode] = True

        for st, end, w in g[bestNode]:
            candidates[end] = min(candidates[end],w + candidates[st])

    return candidates



if __name__ == '__main__':

    N,M = map(int,input().strip().split())
    types = list(map(int,input().strip().split()))

    g = [[] for i in range(N)]

    for _ in range(M):
        a,b,w = map(int,input().strip().split())
        g[a].append((a,b,w))
        g[b].append((b,a,w))

    sol = [float('inf')] * len(set(types))
    for i in range(N):
        candidates = boom(g, i)
        for j in range(N):
            if types[j] == types[i] and candidates[j] != 0 and candidates[j] < sol[types[i]]:
                sol[types[i]] = candidates[j]

    print(*sol)