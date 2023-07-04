

def initial(lab,visited,dataLab):
    for f in range(dataLab['F']):
        for c in range(dataLab['C']):
            if lab[f][c] == 'w':
                visited[f][c] = 1
            if lab[f][c] == 'r':
                dataLab['R'] += 1
            if lab[f][c] == 's':
                dataLab['st_x'] = f
                dataLab['st_y'] = c
                visited[f][c] = 1
            if lab[f][c] == 't':
                desp = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
                for i in range(8):
                    newF = f + desp[i][0]
                    newC = c + desp[i][1]
                    if 0 <= newF < dataLab['F'] and 0 <= newC < dataLab['C']:
                        visited[newF][newC] = 1
                        if lab[newF][newC] == 'r':
                            dataLab['R'] -= 1


def laberintoBT(lab,visited,dataLab,sol,mejorSol,recompensas,f,c):
    if lab[f][c] == 'e' and recompensas == dataLab['R']:
        if sol < mejorSol:
            mejorSol = sol
    else:
        desp = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(4):
            newF = f + desp[i][0]
            newC = c + desp[i][1]
            if 0 <= newF < dataLab['F'] and 0 <= newC < dataLab['C'] and not visited[newF][newC]:
                visited[newF][newC] = 1
                if lab[newF][newC] == 'r':
                    recompensas += 1
                mejorSol = laberintoBT(lab,visited,dataLab,sol+1,mejorSol,recompensas,newF,newC)
                visited[newF][newC] = 0
                if lab[newF][newC] == 'r':
                    recompensas -= 1
    return mejorSol



if __name__ == '__main__':

    F,C = map(int,input().strip().split())

    lab = [[] for _ in range(F)]
    visited = [[0] * C for _ in range(F)]

    for i in range(F):
        l = list(input().strip().split())
        lab[i] = l.copy()

    dataLab = {
        'F' : F,
        'C': C,
        'st_x' : 0,
        'st_y': 0,
        'R': 0
    }

    initial(lab,visited,dataLab)

    sol = 1
    mejorSol = 0x3f3f3f
    recompensas = 0
    print(laberintoBT(lab,visited,dataLab,sol,mejorSol,recompensas,dataLab['st_x'],dataLab['st_y']))
