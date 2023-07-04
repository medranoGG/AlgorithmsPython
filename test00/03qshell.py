

def getBestItem(candidates,d,array):
    bestItem = -1
    bestIndex = -1

    for c in candidates:
        best = array[c] / d["time"][c]
        if best > bestItem:
            bestItem = best
            bestIndex = c

    return bestIndex


def knapsack(d,array):
    n = len(d["b"])
    sol = [-1] * n
    isSol = False
    candidates = set()
    names = []

    for i in range(n):
        candidates.add(i)

    while not isSol and candidates:
        bestCand = getBestItem(candidates,d,array)
        candidates.remove(bestCand)

        if d["time"][bestCand] < d["max_time"]:
            sol[bestCand] = 1
            d["max_time"] -= d["time"][bestCand]
            names.append(d["name"][bestCand])
        else:
            sol[bestCand] = d["max_time"] / d["time"][bestCand]
            names.append(d["name"][bestCand])
            isSol = True

    cont = 0
    for i in range(n):
        if sol[i] != -1:
            cont += sol[i] * array[i]

    return names,cont



if __name__ == '__main__':

    N = int(input().strip())

    for _ in range(N):
        C = input()
        M = int(input().strip())
        T = int(input().strip())

        d = {
            "name" : [],
            "b" : [],
            "i": [],
            "k": [],
            "time": [],
            "max_time" : M
        }

        for _ in range(T):
            var = input()
            o,b,i,k,t = var.split()
            d["name"].append(o)
            d["b"].append(int(b))
            d["i"].append(int(i))
            d["k"].append(int(k))
            d["time"].append(int(t))

        if C == 'kindness':
            names, cont = knapsack(d,d["k"])
            print(*names)
            print("{:.2f}".format(cont))
        elif C == 'intelligence':
            names, cont = knapsack(d,d["i"])
            print(*names)
            print("{:.2f}".format(cont))
        elif C == 'beauty':
            names, cont = knapsack(d,d["b"])
            print(*names)
            print("{:.2f}".format(cont))
