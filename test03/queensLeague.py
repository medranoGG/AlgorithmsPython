import copy


def esSolucion(sol,d,k):
    min = 0x3f3f3f

    for i in range(k,len(d['v'])):
        if d['w'][i] < min:
            min = d['w'][i]

    return min + sol['w'] > d['max_w']


def sumar(d,sol,i):
    sol['obj'][i] = 1
    sol['v'] += d['v'][i]
    sol['w'] += d['w'][i]
    return sol

def restar(d,sol,i):
    sol['obj'][i] = 0
    sol['v'] -= d['v'][i]
    sol['w'] -= d['w'][i]
    return sol


def knapsackBT(d,sol,mejorSol,cont,contbest,k,visited):
    if esSolucion(sol,d,k):
        #print(sol)

        '''
        sum = True
        for s in range(len(sol['obj'])):
            if sol['obj'][s] == 1:
              print(d['n'][s],end=" ")
            
            if visited[s] and sol['obj'][s] == 1:
                sum = False
            elif sol['obj'][s] == 1:
                visited[s] = 1
            
        print()
        '''
        cont += 1
        if sol['v'] > mejorSol['v']:
            mejorSol = copy.deepcopy(sol)
            contbest += 1
        
    else:
        for i in range(k,len(d['v'])):
            if d['w'][i] + sol['w'] <= d['max_w']:
                sol = sumar(d,sol,i)
                mejorSol,cont,contbest = knapsackBT(d,sol,mejorSol,cont,contbest,i+1,visited)
                sol = restar(d, sol, i)

    return mejorSol,cont,contbest



if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    d = {
        'n': [],
        'v': [],
        'w': [],
        'max_w': M
    }

    for _ in range(N):
        name,v,w = input().strip().split()
        d['n'].append(name)
        d['v'].append(int(v))
        d['w'].append(int(w))


    sol = {
        'v': 0,
        'w': 0,
        'obj': [-1]*N
    }
    mejorSol = copy.deepcopy(sol)
    visited = [0] * N

    sol,cont,contBest = knapsackBT(d,sol,mejorSol,0,0,0,visited)
    print(sol['v'],end=" ")
    print(cont-contBest)
    lastSol = []
    namesSol = []
    for i in range(len(sol['obj'])):
        if sol['obj'][i] == 1:
            lastSol.append((d['n'][i],d['w'][i]))
            namesSol.append(d['n'][i])
    namesSol.sort()

    for i in range(len(namesSol)):
        print(namesSol[i],end=" ")
        for j in range(len(lastSol)):
            if namesSol[i] == lastSol[j][0]:
                print(lastSol[j][1])

