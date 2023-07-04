

def dfs(g, disc, low, parent, art_points, cont, act):
    disc[act] = low[act] = cont
    cont += 1
    hijos = 0

    for i in g[act]:
        if disc[i] == -1:
            hijos += 1
            parent[i] = act
            dfs(g, disc, low, parent, art_points, cont, i)
            low[act] = min(low[act], low[i])

            if (parent[act] == -1 and hijos > 1) or (parent[act] != -1 and low[i] >= disc[act]):
                art_points[act] = True

        elif i != parent[act]:
            low[act] = min(low[act], disc[i])


def findArt(g):
    disc = [-1] * N
    low = [-1] * N
    parent = [-1] * N
    art_points = [False] * N
    cont = 0

    for act in range(N):
        if disc[act] == -1:
            dfs(g, disc, low, parent, art_points, cont, act)

    return art_points



if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    g = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().strip().split())
        g[a].append(b)
        g[b].append(a)

    print(findArt(g))
