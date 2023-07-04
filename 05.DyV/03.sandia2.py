

def mergeSandia(mat, l, c):

    n = l
    nn = l
    for i in range(c):
        nn = nn // 2

    f = 0
    i = 0
    matrix = (n * n) // (nn * nn)
    r = matrix // (n // nn)
    s = float('Inf')

    while i < matrix and s != 0:
        for w in range(r):
            columna = 0
            for j in range(r):

                total = 0
                for row in range(f, f+nn):
                    for col in range(columna, columna + nn):
                        total += mat[row][col]

                if total < s:
                    s = total
                i += 1
                columna += nn
                if s == 0:
                    break

            f += nn
            if s == 0:
                break

    print(s)


# Main prog:

N,C = map(int, input().strip().split())

sandia = []

for i in range(N):
    sandia.append([])

for i in range(N):
    file = list(map(int, input().strip().split()))
    sandia[i] += file

mergeSandia(sandia, N, C)
