

def __binarySearchRec__(n, elements, i, j):

    m = (i + j) // 2

    if i > j:
        return -1
    elif elements[m] == n:
        return m
    elif elements[m] < n:
        return __binarySearchRec__(n, elements, m+1, j)
    else:
        return __binarySearchRec__(n, elements, i, m-1)


def binaySearch(n, elements):
    return __binarySearchRec__(n, elements, 0, len(elements)-1)


if __name__ == '__main__':

    N = int(input().strip())
    people = list(map(int,input().strip().split()))
    people.sort()

    M = int(input().strip())
    amoches = list(map(int, input().strip().split()))
    amoches.sort()

    P = int(input().strip())
    comprobar = list(map(int, input().strip().split()))


    for c in comprobar:
        if binaySearch(c, amoches) == -1:
            print(":)")
        else:
            print(":_(")