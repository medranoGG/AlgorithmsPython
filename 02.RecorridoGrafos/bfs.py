from collections import deque


def bfs(g):
    n = len(g)
    visited = [False] * n
    sol = []
    for i in range(n):
        if not visited[i]:
            q = deque()
            q.append(i)
            visited[i] = True
            sol.append(i)
            while q:
                aux = q.popleft()
                for adj in g[aux]:
                    if not visited[adj]:
                        q.append(adj)
                        visited[adj] = True
                        sol.append(adj)
    return sol



if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    g = [ [] for i in range(N)]

    for _ in range(M):
        U, V = map(int, input().strip().split())
        g[U].append(V)

    print(bfs(g))
