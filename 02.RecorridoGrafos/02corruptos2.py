
if __name__ == '__main__':

    N,M = map(int,input().strip().split())

    for _ in range(M):
        A,B = map(int,input().strip().split())

    if (N > 2):
        if (N<=M): # Hay ciclos
            print("CORRUPTOS")
        else:
            print("INOCENTES")
    else:
        print("INOCENTES")
