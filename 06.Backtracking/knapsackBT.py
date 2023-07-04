import copy

def esSolucion(data,sol,k):

    min = 0x3f3f3f
    for i in range(k,len(data['w'])):
        if data['w'][i] < min:
            min = data['w'][i]

    return sol['w'] + min > data['max_w']

def sumar(sol,data,i):
    sol['obj'][i] = 1
    sol['v'] += data['v'][i]
    sol['w'] += data['w'][i]
    return sol


def restar(sol,data,i):
    sol['obj'][i] = 0
    sol['v'] -= data['v'][i]
    sol['w'] -= data['w'][i]
    return sol



def knapsackBT(data,sol,bestSol,k):

    if esSolucion(data,sol,k):
        #print(sol)
        if sol['v'] > bestSol['v']:
            bestSol = copy.deepcopy(sol)
    else:
        for i in range(k,len(data['w'])):
            if data['w'][i] + sol['w'] <= data['max_w']:
                sol = sumar(sol,data,i)
                bestSol = knapsackBT(data,sol,bestSol,i+1)
                sol = restar(sol,data,i)

    return  bestSol




if __name__ == '__main__':

    N, M = map(int,input().strip().split())

    data = {
        'v' : [],
        'w': [],
        'max_w': M
    }

    for _ in range(N):
        l,w,v = input().strip().split()
        data['v'].append(int(v))
        data['w'].append(int(w))


    sol = {
        'obj' : [0] * N,
        'v' : 0,
        'w' : 0
    }

    bestSol = copy.deepcopy(sol)

    print(knapsackBT(data,sol,bestSol,0)['v'])




