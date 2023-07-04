

def initial(lab,visited,dataLab):
    for f in range(dataLab['F']):
        for c in range(dataLab['C']):
            if lab[f][c] == 1:
                visited[f][c] = 1
            if lab[f][c] == 3:
                visited[f][c] = 1
                dataLab['st_f'] = f
                dataLab['st_c'] = c


def laberintoBT(lab,visited,dataLab,sol,bestSol,f,c):
    if lab[f][c] == 4:
        if sol < bestSol:
            bestSol = sol
            print(bestSol)
    else:
        desp1 = [[1,0],[0,1],[-1,0],[0,-1]]
        desp2 = [[2,0],[0,2],[-2,0],[0,-2]]

        for i in range(4):
            newF = f + desp1[i][0]
            newC = c + desp1[i][1]
            newF_doble = f + desp2[i][0]
            newC_doble = c + desp2[i][1]

            if 0 <= newF < dataLab['F'] and 0 <= newC < dataLab['C'] and not visited[newF][newC]:
                visited[newF][newC] = 1
                bestSol = laberintoBT(lab,visited,dataLab,sol+1,bestSol,newF,newC)
                visited[newF][newC] = 0
            elif 0 <= newF_doble < dataLab['F'] and 0 <= newC_doble < dataLab['C'] and not visited[newF_doble][newC_doble] and lab[newF_doble][newC_doble] != 2:
                visited[newF_doble][newC_doble] = 1
                bestSol = laberintoBT(lab, visited, dataLab, sol + 2, bestSol, newF_doble, newC_doble)
                visited[newF_doble][newC_doble] = 0

    return bestSol


if __name__ == '__main__':

    F,C = map(int,input().strip().split())

    lab = [[] for _ in range(F)]
    visited = [[0] * C for _ in range(F)]

    for i in range(F):
        l = list(map(int,input().strip().split()))
        lab[i] = l.copy()

    dataLab = {
        'F' : F,
        'C': C,
        'st_f': 0,
        'st_c': 0
    }

    initial(lab,visited,dataLab)

    sol = 0
    bestSol = 0x3f3f3f

    print(laberintoBT(lab,visited,dataLab,sol,bestSol,dataLab['st_f'],dataLab['st_c']))
