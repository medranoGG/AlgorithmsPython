

def binarySearch(n,elements,i,j):

    m = (i+j) // 2

    if i > j:
        return -i-1
    elif elements[m] == n:
        return m
    elif elements[m] < n:
        return binarySearch(n,elements,m+1,j)
    else:
        return binarySearch(n,elements,i,m-1)


if __name__ == '__main__':

    N = int(input().strip())

    elements = []

    for _ in range(N):
        l = list(map(int,input().strip().split()))
        elements += l

    ataq = list(map(int,input().strip().split()))
    ataq.sort()
    equis = []


    for a in ataq:
        m = binarySearch(a,elements,0,len(elements)-1)

        if m < 0:
            m = -m-1
        equis.append(m)


    for i in range(len(equis)):
        while equis[i] <= equis[i-1] and i != 0:
            equis[i] += 1

        if equis[i] < len(elements):
            elements[equis[i]] = 'X'

    for i in range(0,len(elements),N):
        print(*elements[i:i+N])
