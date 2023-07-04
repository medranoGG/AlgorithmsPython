
def getMinDistance(distances, visied):
    minDist=float('inf')
    minG=0

    for i in range(1,len(distances)):
        if not visied[i] and minDist > distances[i]:
            minDist=distances[i]
            minG=i
    return minG


def dijkstra(g,nodeIn,lista):

    distances= [float('inf')]*len(g)
    visied=[False]*len(g)

    distances[nodeIn]=0


    for _ in range(0,len(g)):
        nextNode=getMinDistance(distances, visied)

        for start, end, weight in g[nextNode]:
            aux = distances[end]
            distances[end] = min(distances[end], distances[start]+weight)
            if aux != distances[end]:
                if lista[start]:
                    lista[end] = lista[start].copy()
                else:
                    lista[end].append(start)
                lista[end].append(end)

        visied[nextNode] = True
    return distances



#Main:
N, M = map(int, input().strip().split())

g = []
lista = []

for i in range(N):
    g.append([])
    lista.append([])

for i in range(M):
    n1, n2, n3 = map(int, input().strip().split())
    g[n1].append((n1, n2 , n3))
    g[n2].append((n2, n1, n3))

S, E = map(int, input().strip().split())

nodeIn= S
sol = dijkstra(g, nodeIn, lista)

print(sol[E])
print(*lista[E])
