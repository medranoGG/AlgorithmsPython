

def initial(lab, visit, dataLab):

    for f in range(dataLab['F']):
        for c in range(dataLab['C']):
            if lab[f][c] == dataLab['P']:
                dataLab['end_x'] = f
                dataLab['end_y'] = c
            elif lab[f][c] == dataLab['P'] + 1:
                visit[f][c] = 1
    visit[0][0] = 1



def laberintoBT(lab, visit, dataLab, piezas, sol, bestSol, f, c):
    if f == dataLab['end_x'] and c == dataLab['end_y'] and piezas == dataLab['P']:
        #print("Encontrado" + str(sol))
        if sol < bestSol:
            bestSol = sol

    else:
        desp = [[1,0],[0,1],[-1,0],[0,-1]]

        for i in range(4):
            newF = f + desp[i][0]
            newC = c + desp[i][1]

            if 0 <= newF < dataLab['F'] and 0 <= newC < dataLab['C'] and not visit[newF][newC] and (lab[newF][newC] == 0 or lab[newF][newC] == piezas+1):
                visit[newF][newC] = 1
                p = piezas + 1
                if lab[newF][newC] == p:
                    piezas += 1
                bestSol = laberintoBT(lab, visit, dataLab, piezas, sol+1, bestSol, newF, newC)
                visit[newF][newC] = 0
                if lab[newF][newC] == p:
                    piezas -= 1

    return bestSol



if __name__ == '__main__':

    F,C,P = map(int,input().strip().split())

    lab = []
    visit = [[0] * C for i in range(F)]

    for _ in range(F):
        l = list(map(int,input().strip().split()))
        lab.append(l)

    dataLab = {
        'F' : F,
        'C': C,
        'P' : P,
        'st_x': 0,
        'st_y': 0,
        'end_x': 0,
        'end_y': 0,
    }

    initial(lab,visit,dataLab)

    sol = 1
    bestSol = 0x3f3f3f
    piezas = 0
    if lab[0][0] == 1:
        piezas = 1
    print(laberintoBT(lab, visit, dataLab, piezas, sol, bestSol, dataLab['st_x'], dataLab['st_y']))
