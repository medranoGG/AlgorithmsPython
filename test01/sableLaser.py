import copy


def initialLab(lab, visited, dataLab):
    for f in range(dataLab['F']):
        for c in range(dataLab['C']):
            if lab[f][c] == 'f':
                visited[f][c] = 0
            elif lab[f][c] == 'w':
                visited[f][c] = 1
            elif lab[f][c] == 'x':
                dataLab['R'] += 1
            elif lab[f][c] == 's':
                dataLab['st_f'] = f
                dataLab['st_c'] = c
                visited[f][c] = 1
            elif lab[f][c] == 'e':
                dataLab['end_f'] = f
                dataLab['end_c'] = c
            else:
                visited[f][c] = 1
                desp = [[-1,0],[1,0],[0,-1],[0,1]]
                if lab[f][c] == 'u':
                    i = 0
                if lab[f][c] == 'd':
                    i = 1
                if lab[f][c] == 'l':
                    i = 2
                if lab[f][c] == 'r':
                    i = 3
                newF = f + desp[i][0]
                newC = c + desp[i][1]
                if 0 <= newF < dataLab['F'] and 0 <= newC < dataLab['C']:
                    visited[newF][newC] = 1
                    if lab[newF][newC] == 'x':
                        dataLab['R'] -= 1


def laberintoBT(lab,visited,dataLab,sol,mejorSol,f,c):
    if f == dataLab['end_f'] and c == dataLab['end_c']:
        print(sol)
        if sol['r'] > mejorSol['r'] or (sol['r'] == dataLab['R'] and sol['p'] < mejorSol['p']):
            mejorSol = copy.deepcopy(sol)
            #print(mejorSol)
    else:
        desp = [[-1,0],[1,0],[0,-1],[0,1]]
        for i in range(4):
            newF = f + desp[i][0]
            newC = c + desp[i][1]

            if 0 <= newF < dataLab['F'] and 0 <= newC < dataLab['C'] and not visited[newF][newC]:
                visited[newF][newC] = 1
                sol['p'] += 1
                if lab[newF][newC] == 'x':
                    sol['r'] += 1
                mejorSol = laberintoBT(lab, visited, dataLab, sol, mejorSol, newF,newC)
                visited[newF][newC] = 0
                sol['p'] -= 1
                if lab[newF][newC] == 'x':
                    sol['r'] -= 1

    return mejorSol


if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    lab = []
    visited = [[0] * M for _ in range(N)]

    for _ in range(N):
        l = list(input().strip().split())
        lab.append(l)

    dataLab = {
        'F' : N,
        'C': M,
        'R': 0,
        'st_f': 0,
        'st_c': 0,
        'end_f': 0,
        'end_c': 0
    }

    initialLab(lab, visited, dataLab)

    sol = {
        'p' : 0,
        'r' : 0
    }

    mejorSol = {
        'p': 0x3f3f3f,
        'r': -1
    }

    best = laberintoBT(lab,visited,dataLab,sol,mejorSol,dataLab['st_f'],dataLab['st_c'])
    print(str(best['r']) + " " + str(best['p']))