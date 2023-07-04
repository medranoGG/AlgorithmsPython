
def getBestItem(candidates,data):
    bestItem = -1
    bestIndex = -1

    for c in candidates:
        best = data["v"][c] / data["w"][c]
        if best > bestItem:
            bestItem = best
            bestIndex = c

    return bestIndex


def knapsack(data):
    n = len(data["v"])
    candidates = set(range(n))
    sol = [0] * n
    esSol = False

    while not esSol and candidates:
        bestCand = getBestItem(candidates,data)
        candidates.remove(bestCand)

        if data["w"][bestCand] <= data["max_w"]:
            sol[bestCand] = 1
            data["max_w"] -= data["w"][bestCand]
        else:
            esSol = True
            sol[bestCand] = data["max_w"] / data["w"][bestCand]

    return sol



if __name__ == '__main__':

    data = {
        "v": [66, 10, 84, 95, 20],  # Valores
        "w": [24, 21, 14, 98, 22],  # Peso
        "max_w": 75  # Peso máximo
    }

    sol = knapsack(data)
    print(sol)






