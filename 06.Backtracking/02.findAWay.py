import copy


def printLab(lab):
    for f in range(len(lab)):
        for c in range(len(lab)):
            if lab[f][c] < 0:
                print("*", end="\t")
            else:
                print(lab[f][c], end="\t")
        print()
    print()

def esSolucion(lab, f, c):
    isSol = True

    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == 0:
                isSol = False

    return f == len(lab)-1 and c == len(lab)-1 and isSol


def laberintoBT(lab, mejorSol, F, C, f, c, k):
    if esSolucion(lab,f,c):#f == F-1 and c == C-1:
        if lab[f][c] < mejorSol[f][c]:
            mejorSol = copy.deepcopy(lab)
    else:
        desp = [[1,0],[0,-1],[0,1],[-1,0]]

        for i in range(len(desp)):
            newF = f + desp[i][0]
            newC = c + desp[i][1]
            if 0 <= newF < F and 0 <= newC < C and lab[newF][newC] == 0:
                lab[newF][newC] = k
                mejorSol = laberintoBT(lab, mejorSol, F, C, newF, newC, k+1)
                lab[newF][newC] = 0

    return mejorSol


if __name__ == '__main__':


    F = int(input().strip())
    C = F

    lab = []

    for i in range(F):
        l = list(map(int,input().strip().split()))
        lab.append(l)

    mejorSol = copy.deepcopy(lab)
    mejorSol[F-1][C-1] = float('inf')

    f = c = 0
    k = 1
    lab[0][0] = k

    mejorSol = laberintoBT(lab, mejorSol, F, C, f, c, k+1)

    if  mejorSol[F-1][C-1] != float('inf'):
        print("SI")
    else:
        print("NO")
