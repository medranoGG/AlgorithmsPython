

def getBestCand(candidates,data):
    bestRatio = -1
    idx = -1
    for c in candidates:
        ratio = data['v'][c] / data['w'][c]
        if ratio > bestRatio:
            bestRatio = ratio
            idx = c

    return idx


def knapsack(data):
    n = len(data['v'])
    candidates = set(range(n))
    sol = [-1] * n
    isSol = False

    while not isSol and candidates:
        bestCand = getBestCand(candidates,data)
        candidates.remove(bestCand)

        if data['w'][bestCand] <= data['max_w']:
            sol[bestCand] = 1
            data['max_w'] -= data['w'][bestCand]
        else:
            sol[bestCand] = data['max_w'] / data['w'][bestCand]
            isSol = True

    return sol


if __name__ == '__main__':

    N, M = map(int,input().strip().split())

    data = {
        'v' : [],
        'w': [],
        'max_w': M
    }

    for _ in range(N):
        w,v = map(int,input().strip().split())
        data['v'].append(v)
        data['w'].append(w)

    sack = knapsack(data)

    sol = []
    cont = 0

    for i in range(len(sack)):
        if sack[i] != -1:
            sol.append(i)
            cont += sack[i] * data['v'][i]

    print(*sol)
    print(round(cont))


