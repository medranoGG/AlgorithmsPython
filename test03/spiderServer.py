

def getBestCand(candidates,visited):
    bestCand = 0x3f3f3f
    idx = -1
    for i in range(len(visited)):
        if not visited[i] and candidates[i] < bestCand:
            bestCand = candidates[i]
            idx = i
    return idx


def dijkstra(g,U):

    n = len(g)
    visited = [False] * n
    candidates =[float('inf')] * n
    roads = [[] for i in range(n)]

    candidates[U] = 0
    visited[U] = True
    for st,end,w in g[U]:
        candidates[end] = w

    for i in range(n-1):
        bestCand = getBestCand(candidates,visited)
        visited[bestCand] = True

        for st,end,w in g[bestCand]:
            if candidates[end] > candidates[st] + w:
                candidates[end] = candidates[st] + w
                if roads[st]:
                    roads[end] = roads[st].copy()
                else:
                    roads[end].append(st)
                roads[end].append(end)
    return candidates,roads


if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    g = [[] for _ in range(N)]

    for _ in range(M):
        a,b,w = map(int,input().strip().split())
        g[a].append((a,b,w))
        g[b].append((b,a,w))

    U = int(input().strip())

    sol,roads = dijkstra(g,U)
    max = max(sol)
    i = sol.index(max)
    print(str(i) + " " + str(max))
    print(*roads[i])

