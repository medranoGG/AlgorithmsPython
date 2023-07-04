
def updateComponents(components, new_id, old_id):
    for i in range(0, len(components)):
        if components[i] == old_id:
            components[i] = new_id


def kruskal(N,candidates):
    candidates.sort()
    components = list(range(N))
    cont = len(components)
    roads = []
    sol = i = 0

    while  cont > 1 and len(candidates) > i:
        (w, st, end) = candidates[i]
        if components[st] != components[end]:
            roads.append((st,end))
            sol += w
            cont -= 1
            updateComponents(components, components[st], components[end])  # Evitar ciclos
        i += 1

    return sol,roads


if __name__ == '__main__':

    N,M = map(int,input().strip().split())
    candidates = []

    for _ in range(M):
        a,b,w = map(int,input().strip().split())
        candidates.append((w,a,b))

    sol,roads = kruskal(N,candidates)
    roads.sort()

    if sol % 5 != 0:
        print(sol // 5 + 1)
    else:
        print(sol/5)
    