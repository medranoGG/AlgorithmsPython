
def getBestCand(candidates,d):
    bestCost = -1
    idx = -1

    for c in candidates:
        ratio = d['v'][c] / d['w'][c]
        if ratio > bestCost:
            bestCost = ratio
            idx = c

    return idx


def knapsack(d):
    n = len(d['e'])
    candidates = set(range(n))
    sol = [-1] * n
    isSol = False

    while not isSol and candidates:
        bestCand = getBestCand(candidates,d)
        candidates.remove(bestCand)

        if d['w'][bestCand] <= d['max_w']:
            sol[bestCand] = 1
            d['max_w'] -= d['w'][bestCand]
        else:
            isSol = True
            #sol[bestCand] = d['max_w'] / d['w'][bestCand]

    return sol



if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    d = {
        'e' : [],
        'v': [],
        'w': [],
        'max_w': M

    }

    for _ in range(N):
        e,v,w = map(int,input().strip().split())
        d['e'].append(e)
        d['v'].append(v)
        d['w'].append(w)

    sol = knapsack(d)
    cont = 0
    for i in range(len(sol)):
        if sol[i] != -1:
            cont += d['v'][i]
    print(cont)
