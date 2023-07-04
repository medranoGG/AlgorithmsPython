
def getBestCand(visited,candidates):
    bestCost = 0x3f3f3f
    idx = -1

    for i in range(len(visited)):
        if not visited[i] and bestCost > candidates[i]:
            bestCost = candidates[i]
            idx = i

    return idx


def dikjstra(g,s):
    n = len(g)
    visited = [False] * n
    candidates = [float('inf')] * n
    roads = [[] for _ in range(n)]

    candidates[s] = 0

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

    N,M = map(int,input().strip().split())

    g = [[] for i in range(N)]

    for _ in range(M):
        a,b,w = map(int,input().strip().split())
        g[a].append((a,b,w))
        g[b].append((b,a,w))

    T = int(input().strip())

    uses = [0] * N

    for _ in range(T):
        s,e = map(int,input().strip().split())
        roads = dikjstra(g,s)
        for r in roads[e]:
            uses[r] += 1

    print(*uses)
