
def binarySearch(elements,n,i,j):

    m = (i + j) // 2

    if i > j:
        return i
    if elements[m] == n:
        return m
    elif elements[m] < n:
        return binarySearch(elements,n,m+1,j)
    else:
        return binarySearch(elements,n,i,m-1)

if __name__ == '__main__':

    N,M = map(int,input().strip().split())
    elements = list(input().strip().split())

    for _ in range(M):
        n = input().strip()
        m = binarySearch(elements,n,0,len(elements)-1)
        print(n + ':' +str(m))
        elements.append(n)
        elements.sort()
    print(*elements)
