
def kruskal(candidates,N):
    candidates.sort()
    components = list(range(N))
    cont = len(components)
    sol = i = 0
    values = [0] * N
    ady_node = [[] for _ in range(N)]

    while cont > 1 and len(candidates) > i:
        (w,st,end) = candidates[i]
        if components[st] != components[end]:
            sol += w
            cont -= 1
            values[st] += w
            values[end] += w
            ady_node[st].append(end)
            ady_node[end].append(st)

            new = components[st]
            old = components[end]
            for j in range(0,len(components)):
                if components[j] == old:
                    components[j] = new
        i += 1
    return sol, values,ady_node



if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    candidates = []

    for _ in range(M):
        a,b,w = map(int,input().strip().split())
        candidates.append((w,a,b))

    sum, values, ady_nodes = kruskal(candidates,N)

    for i in range(len(ady_nodes)):
        ady_nodes[i].sort()

    print("Coste total: " + str(sum))

    for i in range(N):
        print("H" + str(i) + ": " + str(values[i]))
