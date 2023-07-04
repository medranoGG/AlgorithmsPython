from collections import deque


def bfs_groups(g):
    n = len(g)
    visited = [False] * n
    count = 0
    for act in range(n):
        if not visited[act]:
            count += 1
            q = deque()
            q.append(act)
            visited[act] = True
            while q:
                aux = q.popleft()
                for adj in g[aux]:
                    if not visited[adj]:
                        q.append(adj)
                        visited[adj] = True
    print(count)



if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    g = [ [] for _ in range(N)]

    for _ in range(M):
        a,b = map(int,input().strip().split())
        g[a].append(b)
        g[b].append(a)

    bfs_groups(g)