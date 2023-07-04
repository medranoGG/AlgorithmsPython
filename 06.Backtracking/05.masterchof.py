import copy


def esSolucion(sol, pesos, W, k):

    min = 0x3f3f3f
    for i in range(k, len(pesos)):
        if pesos[i] < min:
            min = pesos[i]

    return min + sol['peso'] > W


def sumar(sol,d,i):
    sol['obj'][i] = 1
    sol['peso'] += d['peso'][i]
    sol['benef'] += d['benef'][i]
    return sol


def restar(sol,d,i):
    sol['obj'][i] = 0
    sol['peso'] -= d['peso'][i]
    sol['benef'] -= d['benef'][i]
    return sol


def knapsack(d,sol,mejorSol,k):
    if esSolucion(sol,d['peso'],d['max_peso'],k):#min(d['peso']) + sol['peso'] > d['max_peso']:#
        #print(sol)
        if sol['benef'] > mejorSol['benef']:
            mejorSol = copy.deepcopy(sol)

    else:
        for i in range(k,len(d['names'])):
            if d['peso'][i] + sol['peso'] <= d['max_peso']:
                sol = sumar(sol, d, i)
                mejorSol = knapsack(d, sol, mejorSol, i + 1)
                sol = restar(sol, d, i)

    return mejorSol




if __name__ == '__main__':

    N, C = map(int,input().strip().split())

    d = {
        'names' : [],
        'peso' : [],
        'benef': [],
        'max_peso': C
    }

    for _ in range(N):
        var = input()
        name, T, V = var.split()
        d['names'].append(name)
        d['peso'].append(int(T))
        d['benef'].append(int(V))

    sol = {
        'obj' : [0] * N,
        'peso' : 0,
        'benef' : 0
    }

    mejorSol = copy.deepcopy(sol)

    print(knapsack(d,sol,mejorSol,0)['benef'])