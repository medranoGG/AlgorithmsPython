
# ESTE CÓDIGO SACA CICLOS, PERO DA TIMELIMIT!!
def find_cycles(u, p, color, par, cyclenumber):

    if color[u] == 2:
        return cyclenumber

    if color[u] == 1:
        v = []
        c = p
        v.append(c)

        while c != u:
            c = par[c]
            v.append(c)
        cycles.append(v)
        cyclenumber += 1

        return cyclenumber

    par[u] = p
    color[u] = 1

    for v in g[u]:

        if v != par[u]:
            find_cycles(v, u, color, par, cyclenumber)

    color[u] = 2


if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    g = [ [] for _ in range(N)]
    cycles = []
    color = [0] * N
    par = [0] * N
    cyclenumber = 0

    for _ in range(M):
        A,B = map(int,input().strip().split())
        g[A].append(B)
        g[B].append(A)

    find_cycles(1,0,color,par,cyclenumber)

    if ( cycles != []):
        print("CORRUPTOS")
    else:
        print("INOCENTES")
