
def getBestCand(candidates,visited):
    bestIndex = -1
    cost = 0x3f3f3f

    for i in range(len(visited)):
        if not visited[i] and candidates[i] < cost:
            cost = candidates[i]
            bestIndex = i

    return bestIndex,cost


def bfs(g):
    n = len(g)
    visited = [False] * n
    candidates = [float('inf')] * n
    sol = 0
    roads = []

    init = 0
    ant = 0
    visited[init] = True
    for st,end,w in g[init]:
        candidates[end] = w

    for i in range(n-1):
        bestCand, cost = getBestCand(candidates,visited)

        if cost < float('inf'):
            sol += cost
            visited[bestCand] = True
            roads.append(cost)

        for st,end,w in g[bestCand]:
            if w < candidates[end]:
                candidates[end] = w

    return sol,roads


if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    g = [[] for _ in range(N)]
    solRoads = [[] for i in range(N)]

    for _ in range(M):
        a,b,w = map(int,input().strip().split())
        g[a].append((a,b,w))
        g[b].append((b,a,w))

    sol,costs = bfs(g)
    print(sol)
    print(costs)

    C = int(input().strip())


    for _ in range(C):
        N = int(input().strip())
        print(N)

