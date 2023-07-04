
def kSmallestElement(k,elements):

    piv = elements[k]

    low = [x for x in elements if x < piv]
    if k < len(low):
        return kSmallestElement(k,low)
    k -= len(low)

    equals = [x for x in elements if x == piv]
    if k < len(equals):
        return piv
    k -= len(low)

    high = [x for x in elements if x > piv]
    return kSmallestElement(k, high)



if __name__ == '__main__':

    l = list(map(int,input().strip().split()))
    k = int(input().strip())
    print(kSmallestElement(k,l))
