
def getBestItem(candidates,d):
    bestItem = -1
    bestIndex = -1

    for c in candidates:
        best = d["p"][c] / d["w"][c]
        if best > bestItem:
            bestItem = best
            bestIndex = c

    return bestIndex


def knapsack(d):
    n = len(d["w"])
    sol = [-1] * n
    isSol = False
    candidates = set()

    for i in range(n):
        candidates.add(i)

    while not isSol and candidates:
        bestCand = getBestItem(candidates,d)
        candidates.remove(bestCand)

        if d["w"][bestCand] <= d["w_max"]:
            sol[bestCand] = 1
            d["w_max"] -= d["w"][bestCand]
        else:
            sol[bestCand] = d["w_max"] / d["w"][bestCand]
            isSol = True

    cont = 0
    for i in range(len(sol)):
        if sol[i] != -1:
            cont += d["p"][i] * sol[i]

    return cont

if __name__ == '__main__':

    N,C = map(int,input().strip().split())

    d = {
        "name" : [],
        "w": [],
        "p": [],
        "w_max" : C
    }

    for _ in range(N):
        var = input()
        name,T,V = var.strip().split()
        d["name"].append(name)
        d["w"].append(int(T))
        d["p"].append(int(V))

    sol = knapsack(d)
    print("{:.6f}".format(sol))
