

def getBestTask(candidates,tasks):
    bestValue = 0x3f3f3f
    bestIndex = 0

    for i in candidates:
        if tasks[i] < bestValue:
            bestValue = tasks[i]
            bestIndex = i

    return bestIndex



def orderTasks(tasks):
    candidates = set()
    n = len(tasks)
    sol = []

    for i in range(n):
        candidates.add(i)

    while candidates:
        bestItem = getBestTask(candidates,tasks)
        candidates.remove(bestItem)
        sol.append(bestItem)
    return sol



if __name__ == '__main__':

    tasks = [5, 10, 3]
    sol = orderTasks(tasks)
    print(sol)


