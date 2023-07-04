
def __binarySearchRec(elements,n,i,j):

    m = (i + j) // 2

    if i > j:
        return -1

    if elements[m] == n:
        return m
    if elements[m] < n:
        return __binarySearchRec(elements,n,m+1,j)
    else:
        return __binarySearchRec(elements,n,i,m-1)


def binarySearch(n,elements):
    return __binarySearchRec(elements,n,0,len(elements)-1)


if __name__ == '__main__':

    N1 = int(input())
    g1 = list(map(int,input().strip().split()))
    g1.sort()

    N2 = int(input())
    g2 = list(map(int,input().strip().split()))
    g2.sort()

    M = int(input())

    for _ in range(M):
        sol = []
        a, b = map(int, input().strip().split())
        sol.append(binarySearch(a,g1))
        sol.append(binarySearch(b,g2))

        if (sol[0] == -1 or sol[1] == -1):

            print("SIN DESTINO")
        else:
            print(*sol)