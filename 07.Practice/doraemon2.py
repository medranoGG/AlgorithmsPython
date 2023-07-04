import copy

def esSolucion(sol,d,k):

    ids = 0
    min = 0x3f3f3f

    for i in range(len(d['e'])):
        if sol['obj'][i] == 1:
            ids += d['e'][i]

    for i in range(k,len(d['e'])):
        if min > d['w'][i]:
            min = d['w'][i]


    return ids % 5 == 0 and min + sol['w'] > d['max_w']

def sumar(sol,d,i):
    sol['obj'][i] = 1
    sol['v'] += d['v'][i]
    sol['w'] += d['w'][i]
    return sol

def restar(sol,d,i):
    sol['obj'][i] = 0
    sol['v'] -= d['v'][i]
    sol['w'] -= d['w'][i]
    return sol

def knapsackBT(d,sol,mejorSol,k):
    if esSolucion(sol,d,k):
        print(sol)
        if sol['v'] > mejorSol['v']:
            mejorSol = copy.deepcopy(sol)
    else:
        for i in range(k,len(d['v'])):
            if d['w'][i] + sol['w'] <= d['max_w']:
                sol = sumar(sol,d,i)
                mejorSol = knapsackBT(d, sol, mejorSol, k+1)
                sol = restar(sol,d,i)


    return mejorSol


if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    d = {
        'e' : [],
        'v': [],
        'w': [],
        'max_w': M

    }

    sol = {
        'obj' : [-1] * N ,
        'v': 0,
        'w': 0,
    }
    mejorSol = copy.deepcopy(sol)

    for _ in range(N):
        e,v,w = map(int,input().strip().split())
        d['e'].append(e)
        d['v'].append(v)
        d['w'].append(w)

    sol = knapsackBT(d,sol,mejorSol,0)
    print(sol['v'])
