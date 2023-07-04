

def hamiltonianoVA(g, sol, sol_f, nodo):
    if len(g) + 1 == len(sol) and nodo == sol[0]:
        sol_f.append(sol.copy())
    else:
        for ady in g[nodo]:
            if  ady not in sol or (ady == sol[0] and len(sol) == len(g)):
                sol.append(ady)
                sol_f = hamiltonianoVA(g, sol, sol_f,  ady)
                sol.pop()
    return sol_f



if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    g =[[] for _ in range(N)]

    for _ in range(M):
        a,b = map(int,input().strip().split())
        g[a].append(b)
        g[b].append(a)


    sol = hamiltonianoVA(g, [0], [], 0)
    print(sol)
    print(len(sol))
