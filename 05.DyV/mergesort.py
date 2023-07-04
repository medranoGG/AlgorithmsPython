

def __merge__(left,right,elements):
    l = r = e = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            elements[e] = left[l]
            l += 1
        else:
            elements[e] = right[r]
            r += 1
        e += 1

    if l == len(left):
        a = r
        aux = right
    else:
        a = l
        aux = left

    for i in range(a,len(aux)):
        elements[e] = aux[i]


def mergeSort(l):
    if len(l) < 2:
        return

    m = len(l) // 2
    left = l[:m]
    right = l[m:]
    mergeSort(left)
    mergeSort(right)
    __merge__(left,right,l)


if __name__ == '__main__':

    l = list(map(int,input().strip().split()))
    mergeSort(l)
    print(l)