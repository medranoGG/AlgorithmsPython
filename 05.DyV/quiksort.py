
def partition(v, left, right):
    pivot = v[left]
    i = left + 1
    while i < right and v[i] <= pivot:
        i += 1

    j = right
    while j > left and v[j] > pivot:
        j -= 1

    while i < j:
        v[i], v[j] = v[j], v[i]
        i += 1
        while v[i] <= pivot:
            i += 1

        j -= 1
        while v[j] > pivot:
            j -= 1

    v[left], v[j] = v[j], v[left]
    return j

def qs_rec(arr, left, right):
    if left > right:
        return arr
    else:
        idx = partition(arr, left, right)
        qs_rec(arr, left, idx - 1)
        qs_rec(arr, idx + 1, right)

def quickSort(elements):
    qs_rec(elements, 0, len(elements) - 1)


if __name__ == '__main__':

    l = list(map(int,input().strip().split()))
    quickSort(l)
    print(l)
