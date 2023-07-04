
def inicializar():
    fila = [0]*9
    tablero = []
    for i in range(9):
        tablero.append(fila[:])
    tablero[0][1] = 6
    tablero[0][3] = 1
    tablero[0][5] = 4
    tablero[0][7] = 5
    tablero[1][2] = 8
    tablero[1][3] = 3
    tablero[1][5] = 5
    tablero[1][6] = 6
    tablero[2][0] = 2
    tablero[2][8] = 1
    tablero[3][0] = 8
    tablero[3][3] = 4
    tablero[3][5] = 7
    tablero[3][8] = 6
    tablero[4][2] = 6
    tablero[4][6] = 3
    tablero[5][0] = 7
    tablero[5][3] = 9
    tablero[5][5] = 1
    tablero[5][8] = 4
    tablero[6][0] = 5
    tablero[6][8] = 2
    tablero[7][2] = 7
    tablero[7][3] = 2
    tablero[7][5] = 6
    tablero[7][6] = 9
    tablero[8][1] = 4
    tablero[8][3] = 5
    tablero[8][5] = 8
    tablero[8][7] = 7
    return tablero

def estaEnFila(solucion,fila,num):
    return num in solucion[fila]

def estaEnColumna(solucion,fila, col,num):
    esta = False
    i = 0
    while not esta and i <= fila:
        esta = num == solucion[i][col]
        i += 1
    return esta

def estaEnCuadro(solucion,fila, col,num):
    fInf = 3 * (fila // 3)
    fSup = fInf + 3
    cInf = 3 * (col // 3)
    cSup = cInf + 3
    esta = False
    f = fInf
    while not esta and f < fSup:
        c = cInf
        while not esta and c < cSup:
            esta = num == solucion[f][c]
            c += 1
        f += 1
    return esta

def esFactible(solucion,fila,col,num):
    okFila = not estaEnFila(solucion,fila,num)
    okCol = not estaEnColumna(solucion,fila, col,num)
    okCuadro = not estaEnCuadro(solucion,fila, col,num)
    return okFila and okCol and okCuadro

def esSolucion(sol,i):
    return i >= len(sol)**2

def sudoku(solucion,i):
    if esSolucion(solucion, i):
        esSol = True
    else:
        esSol = False
        fila = i // len(solucion)
        col = i % len(solucion)
        if solucion[fila][col] != 0: # Hay un número inicialmente
            [solucion,esSol] = sudoku(solucion, i + 1)
        else:
            num = 1
            while not esSol and num <= len(solucion):
                if esFactible(solucion, fila, col, num):
                    solucion[fila][col] = num
                    solucion,esSol = sudoku(solucion, i + 1)
                    if not esSol:
                        solucion[fila][col] = 0
                num += 1
    return solucion,esSol

def imprimirSudoku(sudoku):
    print()
    for f in range(len(sudoku)):
        for c in range(len(sudoku)):
            if f % 3 == 0:
                print("----", end="")
        print()
        for c in range(len(sudoku)):
            if c % 3 == 0:
                print("|", end = "")
            print(sudoku[f][c], end='\t')
        print()
    print()


# Prog Ppal:
print("Tablero")
tablero = inicializar()
imprimirSudoku(tablero)
print("Solución")
solucion,esSol = sudoku(tablero, 0)
if esSol:
    imprimirSudoku(solucion)
else:
    print('No se ha encontrado solución')
