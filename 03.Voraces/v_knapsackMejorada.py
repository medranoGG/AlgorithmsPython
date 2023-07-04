

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
    sol = [-1] * n
    visited = [False] * n
    isSol = False
    i = 0

    while not isSol and i < n:
        bestCand = getBestCand(visited,data)
        visited[bestCand] = True

        if data['w'][bestCand] <= data['max_w']:
            sol[bestCand] = 1
            data['max_w'] -= data['w'][bestCand]

        else:
            isSol = True
            sol[bestCand] = data['max_w'] / data['w'][bestCand]

        i += 1

    return sol



if __name__ == '__main__':

    data = {
        "v": [66, 10, 84, 95, 20],  # Valores
        "w": [24, 21, 14, 98, 22],  # Peso
        "max_w": 75  # Peso máximo
    }

    sol = knapsack(data)
    print(sol)






