
def updateComponents(components, new_id, old_id):
    for i in range(0, len(components)):
        if components[i] == old_id:
            components[i] = new_id


def kruskal(N,candidates):
    candidates.sort()
    components = list(range(N))
    cont = len(components)
    sol = i = 0
    values = [0] * N
    ady_nodes = [[] for _ in range(N)]

    while  cont > 0 and N > i:
        (weight, start, end) = candidates[i]
        if components[start] != components[end]:
            values[start] += weight
            values[end] += weight
            ady_nodes[start].append(end)
            ady_nodes[end].append(start)
            sol += weight
            cont -= 1
            updateComponents(components, components[start], components[end])  # Evitar ciclos
        i += 1
    return sol, values, ady_nodes


if __name__ == '__main__':

    N,M = map(int,input().strip().split())
    candidates = []

    for _ in range(M):
        a,b,w = map(int,input().strip().split())
        candidates.append((w,a,b))

    sol, values, ady_nodes = kruskal(N,candidates)
    print(sol)

    C = int(input().strip())

    for _ in range(C):
        N = int(input().strip())
        ady_nodes[N].sort()
        print(str(values[N]) + ":",end=" ")
        print(*ady_nodes[N])