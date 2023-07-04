def dfs(g, disc, moreLow, parent, art_points, cont, act):
    disc[act] = moreLow[act] = cont
    cont += 1
    hijos = 0

    for i in g[act]:
        if disc[i] == -1:
            hijos += 1
            parent[i] = act
            dfs(g, disc, moreLow, parent, art_points, cont, i)
            moreLow[act] = min(moreLow[act], moreLow[i])

            if (parent[act] == -1 and hijos > 1) or (parent[act]!=-1 and moreLow[i]>=disc[act]):
                art_points[act]=True

        elif i!=parent[act]:
            moreLow[act]=min(moreLow[act], disc[i])


def findArt(g):
    disc=[-1] * N
    moreLow = [-1] * N
    parent = [-1] * N
    art_points= [False] * N
    cont = 0

    for act in range(N):
        if disc[act] == -1:
            dfs(g, disc, moreLow, parent, art_points, cont, act)

    return art_points



if __name__ == '__main__':

    N, M = map(int, input().strip().split())
    g = []
    reforces=[]

    for i in range(N):
        g.append([])
        reforces.append(int(input()))

    for i in range(M):
        a,b = map(int,input().strip().split())
        g[a].append(b)
        g[b].append(a)

    art_points = findArt(g)
    print(art_points)
