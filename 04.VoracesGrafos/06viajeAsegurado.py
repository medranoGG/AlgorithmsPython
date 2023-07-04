

def getBestNode(visited,candidates):
    cost = 0x3f3f3f
    bestNode = -1

    for i in range(len(visited)):
        if not visited[i] and candidates[i] < cost:
            cost = candidates[i]
            bestNode = i

    return bestNode


def dijkstra(g,init):
    n = len(g)
    visited = [False] * n
    candidates = [float('inf')] * n

    visited[init] = True
    candidates[init] = 0
    for st, end, w in g[init]:
        candidates[end] = w

    for _ in range(n-1):
        bestNode = getBestNode(visited,candidates)
        visited[bestNode] = True

        for st,end,w in g[bestNode]:
            candidates[end] = min(candidates[end],candidates[st] + w)

    return candidates




if __name__ == '__main__':

    N, M = map(int,input().strip().split())

    g = [[] for i in range(N)]

    for _ in range(M):
        a, b, w = map(int,input().strip().split())
        g[a].append((a,b,w))
        g[b].append((b,a,w))

    sol = set()
    for i in range(N):
        sol.add(max(dijkstra(g,i)))
    print(max(sol))