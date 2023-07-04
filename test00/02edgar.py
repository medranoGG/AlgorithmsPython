
def getBestNode(candidates,visited):
    bestNode = -1
    cost = 0x3f3f3f

    for i in range(len(visited)):
        if not visited[i] and candidates[i] < cost:
            cost = candidates[i]
            bestNode = i

    return bestNode,cost


def dijkstraCaminos(g,D):
    n = len(g)
    visited = [False] * n
    candidates = [float('inf')] * n

    cont = 0
    init = 0
    candidates[init] = 0
    roads = [[] for _ in range(N)]


    for _ in range(n):
        bestNode,cost = getBestNode(candidates,visited)
        visited[bestNode] = True
        cont += cost

        for st,end,w in g[bestNode]:
            if candidates[st] + w < candidates[end]:
                if w <= D:
                    candidates[end] = candidates[st] + w
                    if roads[st]:
                        roads[end] = roads[st].copy()
                    else:
                        if st != 0:
                            roads[end].append(st)

                    roads[end].append(end)

    return roads


if __name__ == '__main__':

    N, M = map(int,input().strip().split())

    g =[[] for _ in range(N)]

    for _ in range(M):
        a,b,w = map(int,input().strip().split())
        a -= 1
        b -= 1
        g[a].append((a,b,w))
        g[b].append((b,a,w))

    C, D = map(int,input().strip().split())
    roads = dijkstraCaminos(g, D)
    print(roads)


    for _ in range(C):
        J = int(input().strip())
        J -= 1
        roads[J].reverse()
        for i in range(len(roads[J])):
            roads[J][i] += 1
        print(*roads[J])
