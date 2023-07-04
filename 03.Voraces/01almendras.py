
def getBestItem(data,candidates):
    bestItem = -1
    bestIndex = -1

    for c in candidates:
        best = data["p"][c] / data["w"][c]
        if best > bestItem:
            bestItem = best
            bestIndex = c

    return bestIndex


def knapsack(data):
    n = len(data["w"])
    candidates = set()
    sol = [-1] * n
    isSol = False

    for i in range(n):
        candidates.add(i)

    while not isSol and candidates:
        bestCand = getBestItem(data,candidates)
        candidates.remove(bestCand)

        if data["w"][bestCand] <= data["w_max"]:
            sol[bestCand] = 1
            data["w_max"] -= data["w"][bestCand]
        else:
            sol[bestCand] = data["w_max"] / data["w"][bestCand]
            isSol = True

    cont = 0
    for i in range(n):
        if sol[i] != -1:
            cont += data["p"][i] * sol[i]
    return cont



if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    data = {
        "p" : [],
        "w" : [],
        "w_max" : 0
    }

    for _ in range(N):
        V,P = map(int,input().strip().split())
        data["p"].append(V)
        data["w"].append(P)

    for _ in range(M):
        MV,MP = map(int,input().strip().split())
        data["w_max"] = MP
        cont = knapsack(data)
        if cont < MV:
            print("TOS")
        else:
            print("PUEDE")