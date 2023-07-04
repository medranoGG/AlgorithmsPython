
def binarySearch(elements,n,i,j):

    m = (i + j) // 2
    if i > j:
        return False
    elif elements[m] == n:
        return m
    elif elements[m] < n:
        return binarySearch(elements,n,m+1,j)
    else:
        return binarySearch(elements,n,i,m-1)


if __name__ == '__main__':
    universos = input().strip().split()
    universos.sort()
    print(universos)

    N = int(input().strip())
    validos = list(range(len(universos)))

    for _ in range(N):
        n = input().strip()
        m = binarySearch(universos,n,0,len(universos)-1)
        ant = m-1
        sig = m+1
        if ant in validos:
            print(universos[ant],end=" ")
        else:
            print("VACIO", end=" ")
        if sig in validos:
            print(universos[sig])
        else:
            print("VACIO")


