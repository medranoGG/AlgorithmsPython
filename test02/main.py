# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("Hello World")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
































"""

##### BFS 

from collections import deque

# 2)
def bfs_aux(v, g, visited):
    q = deque() # Bicola
    visited[v] = True
    q.append(v)
    print("Visiting node " + str(v))
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)
                print("Visiting node " + str(adj))

# 1)
def bfs(g):
    n = len(g)
    visited = [False] * (n)
    for v in range(n):
     if not visited[v]:
            bfs_aux(v, g, visited)


# Main prog:

N,M = map(int,input().strip().split())

g = []

for i in range(N):
    g.append([])

for i in range(M):
    a,b = map(int,input().strip().split())
    g[a].append(b)
    g[b].append(a)


bfs(g)


##### PUNTOS DE ARTICULACION

#2)
def dfs(u,disc,moreLow,parent,p_art,cont,g):
    disc[u]=moreLow[u]=cont
    cont=cont+1
    hijos=0
    for i in g[u]:
        if disc[i]==-1:
            hijos=hijos+1
            parent[i]=u
            dfs(i,disc,moreLow,parent,p_art,cont,g)
            moreLow[u] = min(moreLow[u],moreLow[i])
            if parent[u]==-1 and hijos>1:
                p_art[u]=True
            if parent[u]!=-1 and moreLow[i]>=disc[u]:
                p_art[u]=True
        elif i!=parent[u]:
            moreLow[u]=min(moreLow[u],disc[i])



#1)
def findArt(g,cont,reforces):
    disc=[-1]*N
    moreLow = [-1] * N
    parent = [-1] * N
    p_art=[False]*N
    for i in range(0,N):
        if(disc[i]==-1):
            dfs(i,disc,moreLow,parent,p_art,cont,g)
    total=0
    for i in range(0,N):
        if p_art[i]:
            total=total+reforces[i]
     #print(total)
    print(*p_art)


N, M = map(int, input().strip().split())

g = []
reforces=[]
cont=0

for i in range(0,N):
    g.append([])
    reforces.append(int(input().strip()))

for i in range(0, M):
    a,b=map(int,input().strip().split())
    g[a].append(b)
    g[b].append(a)

findArt(g,cont,reforces)


##### KNAPSACK
def getBestItem(candidates, profit, weight):
    bestItem = -1
    bestRatio = -1

    for i in candidates:
        ratio = profit[i] / weight[i]
        if ratio > bestRatio:
            bestRatio = ratio
            bestItem = i

    return bestItem


def knapsack(weight, profit, MP):
    candidates = set()
    n = len(profit)

    for i in range(n):
        candidates.add(i)

    sol = [-1] * n
    isSol = False

    while candidates and not isSol:
        bestAlm = getBestItem(candidates, profit, weight)
        candidates.remove(bestAlm)

        if weight[bestAlm] <= MP:
            MP -= weight[bestAlm]
            sol[bestAlm] = 1
        else:
            sol[bestAlm] = MP / weight[bestAlm]
            isSol = True

    return sol


#main:

n= 5
data= {} # Me creo un diccionario. Puede ser un array!
data['profit'] = [66,10,84,95,20] # Valores
data['weight'] = [24,21,14,98,22] # Peso
data['maxWeight'] = 75 # Peso máximo de mi mochila

# No tiene sentido ordenarlos.

sol = knapsack(data['weight'],data['profit'],data['maxWeight'])

print(sol)


##### SCHEDULE

def getBestDate(candidates, profit):
    bestItem = -1
    bestProfit = -1

    for i in candidates:
        if profit[i] > bestProfit:
            bestProfit = profit[i]
            bestItem = i

    return bestItem


def schedule(profit ,dates):

    candidates = set()
    n = len(profit)

    for i in range(n):
        candidates.add(i)

    m = int(max(dates)) + 1
    sol = [-1] * m
    j = m

    while j > 0 and candidates:
        bestItem = getBestDate(candidates, profit)
        candidates.remove(bestItem)

        found = False
        i = dates[bestItem]

        while i >= 0 and not found:
            if sol[i] == -1:
                sol[i] = bestItem
                found = True
            i -= 1
        j -= 1

    return sol


#Main prog:

profit= [50,10,15,30] #Beneficio
deadLine= [2,1,2,1]   #Fecha tope

schedule=schedule(profit,deadLine)
print(schedule) # No imprimo len(candidates), sino el max


##### TIME CANDIDATOS
def getBestStack(candidates, tasks):
    bestStack = -1
    bestTime = 0x3f3f3f3

    for i in candidates:
        if tasks[i] < bestTime:
            bestTime = tasks[i]
            bestStack = i

    return bestStack


def orderTasks(tasks):
    candidates = set()
    n = len(tasks)

    for i in range(n):
        candidates.add(i)

    sol = []

    while candidates:
        bestStack = getBestStack(candidates, tasks)
        candidates.remove(bestStack)
        sol.append(bestStack)

    return sol


def waitingTime(tasks, sol):
    times = []
    timesT = []
    for i in sol:
        times.append(tasks[i])
        timesT += times

    return timesT

tasks = [5,10,3]

tasks.sort()

sol = orderTasks(tasks)
w = waitingTime(tasks, sol)
print(sol) # Orden
print(sum(w)) # Tiempo total

#sorted(stack)


##### DIJKSTRA
def getBestNode(candidates, visited):
    bestNode = -1
    bestWeight = 0x3f3f3f

    for i in range(len(candidates)):
        if not visited[i] and candidates[i] < bestWeight:
            bestWeight = candidates[i]
            bestNode = i

    return bestNode


def dijkstra(g, initial):
    n = len(g)
    candidates = [float('inf')] * n  # Candidates = sol
    visited = [False] * n

    visited[initial] = True
    candidates[initial] = 0

    for st, end, w in g[initial]:
        candidates[end] = w

    for i in range(n):
        bestNode = getBestNode(candidates, visited)
        visited[bestNode] = True

        for st, end, w in g[bestNode]:
            candidates[end] = min(candidates[end], candidates[st] + w)

    
    return candidates


# Main prog:

N,M=map(int,input().strip().split())

g=[]

for i in range(N):
    g.append([])


for i in range(M):
    n1,n2,n3=map(int,input().strip().split())
    g[n1].append((n1,n2,n3))
    g[n2].append((n2,n1,n3))



node = 0
sol = dijkstra(g, node)

print(sol)


##### PRIM
def getBestNode(candidates, visited):
    bestNode = -1
    bestWeight = float('inf')

    for i in range(len(candidates)):
        if not visited[i] and candidates[i] < bestWeight:
            bestWeight = candidates[i]
            bestNode = i

    return bestNode


def prim(g):
    n = len(g)
    candidates = [float('inf')] * n
    visited = [False] * n

    sol = 0

    init = 0
    visited[init] = True

    for st, end, w in g[init]:
        candidates[end] = w

    for i in range(1, len(candidates)):
        bestNode = getBestNode(candidates, visited)

        if candidates[bestNode] != float('inf'):
            sol += candidates[bestNode]
            visited[bestNode] = True

        for st, end, w in g[bestNode]:
            if not visited[end]:
                candidates[end] = min(candidates[end], w)

    return sol

# Main prog:

N,M=map(int,input().strip().split())


g=[]

for i in range(N+1):
    g.append([])


for i in range(M):
    n1,n2,n3=map(int,input().strip().split())
    g[n1].append((n1,n2,n3))
    g[n2].append((n2,n1,n3))

sol=prim(g)
print(sol)


##### BINARY SEARCH

# Buscamos elemento el lista ORDENADA, si no está, devuelvo -1.

def __binSearch__(array,e,i,j):

    if i > j:
        return -1

    m = (i + j) // 2

    if array[m] == e:
        return m

    elif array[m] > e:
        return __binSearch__(array,e,i,m-1)
    else:
        return __binSearch__(array, e, m + 1, j)


def binarySearch(array , e):
    i=0
    j=len(array)-1
    return __binSearch__(array,e,i,j)

#Main:

N = int(input())
group1 = list(map(int,input().strip().split()))

group1.sort()

index = binarySearch(group1,N)

print(index) # Devuelvo -1 si no está


##### MERGESHORT

# Ordenamos vector con técnica de división

def merge(first, second, out):
    f = s = k = 0
    while f < len(first) and s < len(second):
        if first[f] <= second[s]:
            out[k] = first[f]
            f += 1
        else:
            out[k] = second[s]
            s += 1
        k += 1

    if s == len(second):
        r = f
        remainder = first

    else:
        r = s
        remainder = second

    for i in range(r,len(remainder)):
        out[k] = remainder[i]
        k += 1


def mergeSort(input):
    if len(input) < 2:
        return

    mid = len(input) // 2
    left = input[:mid]
    right = input[mid:]
    mergeSort(right)
    mergeSort(left)


    merge(left, right, input)

#Main:
l = [4,3,2,5,1]

mergeSort(l)
print(l)


##### KSMALLEST ELEMENT

# Calculo el k-ésimo menor elemento en array no ordenado!!
# input ->  8 4 6 2 10 , busco 3o
# output -> 6

def kSmallestElement(k, elements):

    pivot = elements[k]

    low = [x for x in elements if x < pivot]
    #######################################
    if k < len(low):
        return kSmallestElement(k, low)
    k -= len(low)


    equals = [ x for x in elements if x == pivot]
    #######################################
    if k < len(equals):
        print(pivot)
        return pivot
    k -= len(equals)

    high = [ x for x in elements if x > pivot]
    #######################################
    return kSmallestElement(k,high)



# Main prog:

elements = list(map(int,input().strip().split()))


medium = (len(elements) - 1) // 2

kSmallestElement(2, elements)


##### SUMA M ELEMENTOS


def esSolucion(W, M, sol, k):
    sum = 0
    for i in range(k+1):
        if sol[i] == 1:
            sum += W[i]
    return sum == M


def esFactible():
    sum = 0
    for i in range(k+1):
        if sol[i] == 1:
            sum += W[i]
    return sum <= M




def vueltaAtrasSubconjuntos(W, M, sol, k):
    if esSolucion(W, M, sol, k):
        print(sol)
    else:
        if k < len(sol) - 1:
            k = k + 1
            vueltaAtrasSubconjuntos(W, M, sol, k)
            if esFactible():
                sol[k] = 1
                vueltaAtrasSubconjuntos(W, M, sol, k)
                sol[k] = 0



# Main prog:


W = [7, 2, 3, 4, 9]
M = 9
sol = [0] * len(W)
k = -1
vueltaAtrasSubconjuntos(W, M, sol, k)


##### COLOREADO
# CORRECTO, MYCODE:



def coloreado(g, sol, nodo, m):
    if nodo == len(sol): # si es sol
        esSol = True
    else:
        esSol = False
        color = 1
        while not esSol and color <= m:
            if esFactible(g, sol, nodo, color):
                sol[nodo] = color
                esSol, sol = coloreado(g, sol, nodo+1, m)
                if not esSol:
                    sol[nodo] = 0
            color += 1

    return esSol, sol


def esFactible(g, sol, nodo, color):
    isfact = True
    i = 0
    ady = g[nodo]

    while isfact and i < len(ady):
        if ady[i] < nodo:
            isfact = (color != sol[ady[i]])
        i += 1

    return isfact


#Main prog:

N, M = map(int, input().strip().split())
g= []

for i in range(N):
    g.append([])

for v in range(0, M):
    A, B = map(int, input().strip().split())
    g[A].append(B)
    g[B].append(A)

m = 4 # Numero de colores disponibles
nodo = 0 # Nodo inicial
sol = [0] * N

esSol, sol = coloreado(g, sol, nodo, m)

if esSol:
    print(sol)
else:
    print("No se encuentra solución")
    

##### HAMILTONIANO

# MY CODE:

def esSol(g, sol, nodo):
    return len(g)+1 == len(sol) and nodo == sol[0]

def esFactible(nodo, sol, n):
    return nodo not in sol or (nodo == sol[0] and len(sol) == n)

def hamiltoniano(g, nodo, sol, numSol):

    if esSol(g, sol, nodo):
        print(sol)
        numSol += 1

    else:

        for ady in g[nodo]:
            if esFactible(ady, sol, len(g)):
                sol.append(ady)
                numSol = hamiltoniano(g, ady, sol, numSol)
                sol.remove(ady)

    return numSol




#Main prog:

N, M = map(int, input().strip().split())
g= []

for i in range(N):
    g.append([])

for v in range(M):
    A, B = map(int, input().strip().split())
    g[A].append(B)
    g[B].append(A)

init = 0
numSol = 0
sol = [init]
hamiltoniano(g,init,sol,numSol)


##### KNAPSACK BT
import copy

def knapsack(sol, mejorSol, pesos, valor, W, k):


    if esSolucion(sol, pesos, W):
        if sol['valor'] > mejorSol['valor']:
            mejorSol = copy.deepcopy(sol)
        else:
            mejorSol = copy.deepcopy(mejorSol)
        

    else:
        for i in range(k,len(pesos)):
            if (sol['peso'] + pesos[i] <= W): # Es factible
                sol = asignar(sol, i, valor, pesos)
                mejorSol= knapsack(sol, mejorSol, pesos, valor, W, i+1)
                sol = borrar(sol, i, valor, pesos)

    return mejorSol



def esSolucion(sol, pesos, W):
    return min(pesos) + sol['peso'] > W


def mejor(sol1,sol2):
    if sol1['Valor'] > sol2['Valor']:
        best = copy.deepcopy(sol1)
    else:
        best = copy.deepcopy(sol2)

    return best


def asignar(sol, i, valor, pesos):
    sol['objetos'][i] = 1
    sol['valor'] += valor[i]
    sol['peso'] += pesos[i]
    return sol

def borrar(sol, i, valor, pesos):
    sol['objetos'][i] = 0
    sol['valor'] -= valor[i]
    sol['peso'] -= pesos[i]
    return sol


# Main prog:

W = 8  # Peso máximo.
pesos = [2, 3, 4, 5]
valor = [3, 5, 6, 10]
k = 0
sol = {}
sol['objetos'] = [0] * len(pesos)
sol['valor'] = 0
sol['peso'] = 0

mejorSol = copy.deepcopy(sol)


print(knapsack(sol, mejorSol, pesos, valor, W, k))


##### LABERINTO
import copy

def printLab(lab):
    for f in range(len(lab)):
        for c in range(len(lab)):
            if lab[f][c] < 0:
                print("*", end="\t")
            else:
                print(lab[f][c], end="\t") # Con fin en espacio.
        print()
    print()

#########################################################################################################


def esSolucion(lab, f, c):
    return f == len(lab)-1 and c == len(lab)-1


def esFactible(lab, f, c):
    return 0 <= f < len(lab) and 0 <= c < len(lab) and lab[f][c] == 0


def esMejor(sol1,sol2):
    n = len(sol1)-1
    return sol1[n][n] < sol2[n][n]


def laberinto(lab, mejorSol, f, c, k):

    if esSolucion(lab, f, c):
        #printLab(lab)
        if esMejor(lab,mejorSol):
            mejorSol = copy.deepcopy(lab)

    else:
        desp = [[0,1],[0,-1],[1,0],[-1,0]]
        #desp = [[-1,-1], [1,-1], [-1,1], [1,1]]
        i = 0

        while i < len(desp):
            newF = f + desp[i][0]
            newC = c + desp[i][1]
            if esFactible(lab, newF, newC):
                lab[newF][newC] = k
                mejorSol = laberinto(lab, mejorSol, newF, newC, k+1)
                lab[newF][newC] = 0
            i += 1

    return mejorSol



# Main prog:



N = int(input())

lab = []

for i in range(N):
    lab.append([])

for i in range(N):
    l = list(map(int,input().strip().split()))
    lab[i] += l

bestSol = copy.deepcopy(lab)
bestSol[len(lab)-1][len(lab)-1] = float('inf') # Si el ultimo es infinito, no habrá sol.

f = 0
c = 0
k = 1

lab[f][c] = k

bestSol = laberinto(lab, bestSol, f, c, k+1) # lab primero a 1, bestSol ultimo a inf
                                             # f=0, c=0, k=2

print("MEJOR:")
printLab(bestSol)


##### LEAPDAY
import copy

def esSolucion(lab, f, c):
    return lab[f][c] == 4

def esFactible1(lab, f, c, N, M):
    if (0 <= f < N and 0 <= c < M):
        if (lab[f][c] == 0 or lab[f][c] == 2 or lab[f][c] == 4) and (labSol[f][c] == 0):
            return True
        else:
            return False
    return False


def esFactible2(lab, f, c, N, M):
    if (0 <= f < N and 0 <= c < M):
        if lab[f][c] == 0 and (labSol[f][c] == 0):
            return True
        else:
            return False
    return False



def laberintoLD(lab, labSol, bestSol, f, c, k, N , M):

    if esSolucion(lab, f, c):

        if labSol[f][c] < bestSol[f][c]:
            bestSol = copy.deepcopy(labSol)

    else:
        desp = [[0,1],[1,0],[0,-1],[-1,0]]
        despDoble = [[0, 2], [2, 0], [0, -2], [-2, 0]]
        i = 0
        while i < len(desp):
            newF = f + desp[i][0]
            newC = c + desp[i][1]
            newFD = f + despDoble[i][0]
            newCD = c + despDoble[i][1]

            #if k < bestSol[f2][c2]

            if esFactible1(lab, newF, newC, N, M):

                labSol[newF][newC] = k
                bestSol = laberintoLD(lab, labSol, bestSol, newF, newC, k+1, N , M)
                labSol[newF][newC] = 0

            elif esFactible2(lab, newFD, newCD, N, M):

                    k += 1
                    labSol[newFD][newCD] = k
                    bestSol = laberintoLD(lab, labSol, bestSol, newFD, newCD, k+1, N , M)
                    labSol[newFD][newCD] = 0
                    k -= 1
            i += 1

    return bestSol



# Main prog:

N, M = map(int,input().strip().split())

lab = []
labSol = []

for i in range(N):
    lab.append([])
    labSol.append([])

for i in range(N):
    l = list(map(int,input().strip().split()))
    lab[i] += l

k = 1



for i in range(N):
    for j in range(M):
        labSol[i].append(0)

bestSol = copy.deepcopy(labSol)

for i in range(N):
    for j in range(M):
        if lab[i][j] == 3:
            f = i
            c = j
        if lab[i][j] == 4:
            f2 = i
            c2 = j

bestSol[f2][c2] = float('inf')





bestSol= laberintoLD(lab, labSol, bestSol, f, c, k, N , M)

print(bestSol[f2][c2])


"""
