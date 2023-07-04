from collections import deque


def bfs_groups(g):
    n = len(g)
    visited = [False] * n
    for act in range(n):
        l = []
        if not visited[act]:
            q = deque()
            q.append(act)
            visited[act] = True
            l.append(act)

            while q:
                aux = q.popleft()
                for adj in g[aux]:
                    if not visited[adj]:
                        q.append(adj)
                        visited[adj] = True
                        l.append(adj)
            l.sort()
            print(*l)




if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    g = [ [] for _ in range(N)]

    for _ in range(M):
        A, B = map(int, input().strip().split())
        g[A].append(B)
        g[B].append(A)

    bfs_groups(g)