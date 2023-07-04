
def binarySearchRec(l,n,i,j):

    m = (i + j) // 2
    if i > j:
        return -1 # -i-1
    elif l[m] == n:
        return m
    elif l[m] < n:
        return binarySearchRec(l,n,m+1,j)
    else:
        return binarySearchRec(l,n,i,m-1)



if __name__ == '__main__':

    l = list(map(int,input().strip().split()))
    l.sort() # SIEMPRE
    n = int(input().strip())

    print(binarySearchRec(l,n,0,len(l)-1))

'''
1 4 2 5 3 8 6 9
5
'''