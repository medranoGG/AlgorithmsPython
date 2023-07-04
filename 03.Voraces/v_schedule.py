

def getBestItem(candidates,profit): # max
    bestItem = -1
    bestIndex = -1

    for c in candidates:
        if profit[c] > bestItem:
            bestItem = profit[c]
            bestIndex = c

    return bestIndex


def schedule(profit,deadLine):
    n = len(profit)
    candidates = set(range(n))
    maxDate = max(deadLine)
    sol = [-1] * (maxDate + 1)

    while maxDate >= 0 and candidates:
        bestCand = getBestItem(candidates,profit)
        candidates.remove(bestCand)
        found = False
        j = deadLine[bestCand]
        while not found and j >= 0:
            if sol[j] == -1:
                sol[j] = bestCand
                found = True
            j -= 1
        maxDate -= 1
    return sol



if __name__ == '__main__':

    profit = [50, 10, 15, 30]  # Beneficio
    deadLine = [2, 1, 2, 1]  # Fecha tope

    sol = schedule(profit,deadLine)
    print(sol)