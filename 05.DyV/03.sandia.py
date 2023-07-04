
def merge(sandia,C):
    if C == 0:
        return sum(sandia)

    l1 = []
    l2 = []
    l3 = []
    l4 = []
    m = len(sandia) // 2
    mm = m // 2
    mmm = mm // 2
    left = sandia[:m]
    left1 = left[:mm]
    left2 = left[mm:]
    l1 = left1[:mmm] + left2[:mmm]
    l2 = left1[mmm:] + left2[mmm:]


    right = sandia[m:]
    right1 = right[:mm]
    right2 = right[mm:]
    l3 = right1[:mmm] + right2[:mmm]
    l4 = right1[mmm:] + right2[mmm:]


    C -= 1
    return min(merge(l1,C),merge(l2,C),merge(l3,C),merge(l4,C))


if __name__ == '__main__':

    N,C = map(int,input().strip().split())

    sandia = []

    for i in range(N):
        var = list(map(int,input().strip().split()))
        sandia += var

    print(merge(sandia,C))


