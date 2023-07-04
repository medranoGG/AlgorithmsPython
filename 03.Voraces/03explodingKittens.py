

def getBestItem(d,candidates):
    bestItem = -1
    bestIndex = -1

    for c in candidates:
        best = d["profit"][c] / d["risk"][c]
        if best > bestItem:
            bestItem = best
            bestIndex = c

    return bestIndex


def knapsack(d):
    n = len(d["name"])
    candidates = set()
    isSol = False
    sol = []

    for i in range(n):
        candidates.add(i)

    while not isSol and candidates:
        bestCand = getBestItem(d,candidates)
        candidates.remove(bestCand)

        if d["risk"][bestCand] <= d["max_risk"]:
            sol.append(d["name"][bestCand])
            d["max_risk"] -= d["risk"][bestCand]
        else:
            isSol = True
            sol.append(d["name"][bestCand])

    return sol


if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    d = {
        "name" : [],
        "risk" : [],
        "profit" : [],
        "max_risk" : M
    }

    for _ in range(N):
        var = input()
        C, R, B = var.strip().split()
        d["name"].append(C)
        d["risk"].append(int(R))
        d["profit"].append(int(B))

    sol = knapsack(d)
    print(*sol)