def find_cycles(u, p, color, par, cycles):
    if color[u] == 2:
        return cycles

    if color[u] == 1:
        v = [p]
        c = p
        while c != u:
            c = par[c]
            v.append(c)
        cycles.append(v)
        return cycles

    par[u] = p
    color[u] = 1

    for v in g[u]:
        if v != par[u]:
            find_cycles(v, u, color, par, cycles)

    color[u] = 2
    return cycles


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    g = [[] for _ in range(N)]
    color = [0] * N
    par = [0] * N
    cycles = []

    for _ in range(M):
        A, B = map(int, input().strip().split())
        g[A].append(B)
        g[B].append(A)

    print(find_cycles(1, 0, color, par, cycles))
