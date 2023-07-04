import math


def getBestCand(visited,data):
    best = -1
    idx = -1

    for i in range(len(visited)):
        ratio = data['v'][i] / data['w'][i]
        if not visited[i] and ratio > best:
            best = ratio
            idx = i

    return idx


def knapsack(data):
    n = len(data['w'])
    candidates = [-1] * n
    visited = [False] * n
    isSol = False
    i = 0

    tres = []

    while not isSol and i < n:
        bestCand = getBestCand(visited,data)
        visited[bestCand] = True

        if data['w'][bestCand] <= data['max_w']:
            candidates[bestCand] = 1
            data['max_w'] -= data['w'][bestCand]
            if i < 3:
                tres.append(bestCand)

        else:
            isSol = True
            candidates[bestCand] = data['max_w'] / data['w'][bestCand]
            if i < 3:
                tres.append(bestCand)

        i += 1

    return candidates, tres


'''
if __name__ == '__main__':

    N = int(input().strip())

    data = {
        'i' : [],
        'v': [],
        'w': [],
        'max_w': 0
    }

    for _ in range(N):
        i, c, h = map(int,input().strip().split())
        data['i'].append(i)
        data['v'].append(c)
        data['w'].append(h)

    data['max_w'] = int(input().strip())

    sol,tres = knapsack(data)
    v_tot = 0
    f_tot = 0
    for i in range(len(sol)):
        if sol[i] != -1:
            v_tot += sol[i] * data['v'][i]
        if sol[i] == 1:
            f_tot += data['w'][i]


    print(math.ceil(v_tot),end=" ")
    print(math.ceil(f_tot))
    for i in range(3):
        print(tres[i])
'''
if __name__ == '__main__':

    data = {
        "v": [66, 10, 84, 95, 20],  # Valores
        "w": [24, 21, 14, 98, 22],  # Peso
        "max_w": 75  # Peso máximo
    }

    sol = knapsack(data)
    print(sol[0])

