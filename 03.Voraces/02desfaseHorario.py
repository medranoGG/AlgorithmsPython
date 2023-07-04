

def getBestItem(data,candidates):
    bestItem = 0x3f3f3f
    bestIndex = -1

    for c in candidates:
        if data["F"][c] < bestItem:
            bestItem = data["F"][c]
            bestIndex = c

    return bestIndex


def schedule(data):
    n = len(data["I"])
    candidates = set()
    maxDate = max(data["F"])
    count = 0
    last = -1

    for i in range(n):
        candidates.add(i)


    while candidates:
        bestCand = getBestItem(data,candidates)
        candidates.remove(bestCand)
        if data["I"][bestCand] > last:
            count +=1
            last = data["F"][bestCand]

    return count


if __name__ == '__main__':

    N = int(input().strip())

    data = {
        "name" : [],
        "I" : [],
        "F" : []
    }

    for _ in range(N):
        var = input()
        name, I, F = var.split()
        data["name"].append(name)
        data["I"].append(int(I))
        data["F"].append(int(F))

    sol = schedule(data)
    print(sol)
