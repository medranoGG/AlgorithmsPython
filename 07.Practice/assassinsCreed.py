def getBestCand(visited,candidates):
    bestCost = 0x3f3f3f
    idx = -1

    for i in range(len(visited)):
        if not visited[i] and candidates[i] < bestCost:
            bestCost = candidates[i]
            idx = i

    return idx


def dijkstra(g,init):
    n = len(g)
    visited = [False] * n
    candidates = [float('inf')] * n
    roads = [[] for _ in range(n)]

    visited[init] = True
    candidates[init] = 0
    for s,e,w in g[init]:
        candidates[e] = w
        roads[e].append(s)
        roads[e].append(e)

    for _ in range(n-1):
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
    return roads,candidates


if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    g =[[] for _ in range(N)]

    for _ in range(M):
        a,b,w = map(int,input().strip().split())
        g[a].append((a,b,w))
        g[b].append((a,b,w))

    R = int(input())
    inaccesibles = list(map(int,input().strip().split()))
    s,e = map(int,input().strip().split())

    sol, candidates = dijkstra(g,s)
    imp = False

    for s in sol[e]:
        if s in inaccesibles:
            imp = True

    if imp:
        print('IMPOSIBLE')
    else:
        print(candidates[e])
