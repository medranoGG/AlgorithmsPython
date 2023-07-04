from collections import deque


def bfs_casting(g):
    n = len(g)
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            q = deque()
            q.append(i)
            visited[i] = True
            while q:
                aux = q.popleft()
                for adj in g[aux]:
                    if not visited[adj]:
                        q.append(adj)
                        visited[adj] = True

    if (count != 1):
        return False
    else:
        return True


if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    g = [ [] for i in range(N)]
    gInv = [ [] for i in range(N)]

    for _ in range(M):
        U, V = map(int, input().strip().split())
        g[U].append(V)
        gInv[V].append(U)


    if (bfs_casting(g) and bfs_casting(gInv)):
        print("CASTING COMPLETO")
    else:
        print("HAY QUE REPETIR")