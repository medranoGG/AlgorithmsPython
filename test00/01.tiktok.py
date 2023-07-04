from collections import deque


def tiktok(g,level):
    n = len(g)
    visited = [False] * n
    colors = [0] * n
    q = deque()
    sol = 0

    if not visited[0]:
        q.append(0)
        visited[0] = True

        while q:
            aux = q.popleft()
            reach = colors[aux]

            for adj in g[aux]:
                if not visited[adj]:
                    q.append(adj)
                    visited[adj] = True
                    colors[adj] = reach + 1 # Cojo el anterior y le sumo 1

    for c in colors:
        if c < level:
            sol += 1

    return sol



if __name__ == '__main__':

    N = int(input().strip())

    for _ in range(N):
        M, K, C = map(int,input().strip().split())

        g = [[] for _ in range(K)]

        for _ in range(C):
            a,b = map(int,input().strip().split())
            g[a].append(b)
            g[b].append(a)

        print(tiktok(g,M))
