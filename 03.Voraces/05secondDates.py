
def getBestItem(d,candidates):
    bestItem = 0x3f3f3f
    bestIndex = -1

    for c in candidates:
        if d["a"][c] < bestItem:
            bestItem = d["a"][c]
            bestIndex = c

    return bestIndex

def voraz(d):
    n = len(d["n"])
    solP = []
    solG = []
    candidates = set()

    for i in range(n):
        candidates.add(i)

    while candidates:
        bestCand = getBestItem(d,candidates)
        candidates.remove(bestCand)

        if d["g"] > 0:
            solP.append(d["n"][bestCand])
            d["g"] -= 1
        else:
            solG.append(d["n"][bestCand])

    print(*solP)
    print(*solG)



if __name__ == '__main__':

    N, K = map(int,input().strip().split())

    k = N - K
    if k < K:
        K = k


    d = {
        "n" : [],
        "a" : [],
        "g" : K
    }

    for _ in range(N):
        var = input()
        C, A = var.strip().split()
        d["n"].append(C)
        d["a"].append(int(A))

    sol = voraz(d)
