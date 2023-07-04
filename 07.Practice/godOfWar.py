

def binarySearch(n,elements,i,j):

    m = (i + j) // 2

    if i > j:
        return -i
    elif elements[m] == n:
        return m
    elif elements[m] < n:
        return  binarySearch(n,elements,m+1,j)
    else:
        return  binarySearch(n,elements,i,m-1)

if __name__ == '__main__':

    N = int(input().strip())
    valids = list(range(N))

    elements = list(map(int,input().strip().split()))

    N = int(input().strip())

    find = list(map(int,input().strip().split()))

    for f in find:
        m = binarySearch(f,elements,0,len(elements) - 1)
        if m > 0:
            if m-1 in valids:
                print(str(elements[m-1]) + " X")
        else:
            m = -m
            if m-1 in valids:
                print(str(elements[m-1]),end=" ")
            else:
                print("X ",end=" ")
            if m in valids:
                print(str(elements[m]))
            else:
                print(" X")


