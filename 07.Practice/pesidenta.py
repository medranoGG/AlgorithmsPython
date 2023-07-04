

def kruskal(candidates, N):
    candidates.sort()
    components = list(range(N))
    sol = i = 0
    cont = len(components)
    roads = []

    while cont > 1 and len(candidates) > i:
        (w,st,end) = candidates[i]
        if components[st] != components[end]:
            roads.append((st,end))
            cont -= 1
            sol += w

            old = components[end]
            new = components[st]
            for j in range(len(components)):
                if components[j] == old:
                    components[j] = new

        i += 1

    return sol,roads



if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    candidates = []
    components = []

    for _ in range(M):
        a, b, w = input().strip().split()
        w = int(w)
        if a not in components:
            components.append(a)
        if b not in components:
            components.append(b)
        candidates.append((w,components.index(a),components.index(b)))


    sol, roads = kruskal(candidates, N)
    print(sol)
    solRoads = []
    for i in range(len(roads)):
        solRoads.append((components[roads[i][0]], components[roads[i][1]]))

    solRoads.sort()
    for i in range(len(solRoads)):
        print(solRoads[i][0] + " - " + solRoads[i][1])
