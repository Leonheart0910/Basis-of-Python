def rotate(L, K):
    #어떤 리스트 L을 K번 왼쪽,
    #K 가 음수면 오른쪽,
    if K > 0:
        Q = len(L) - K + 1
        i = 0

        while(i < Q-1):
            W = L.pop(0)
            L.append(W)
            i += 1

L = [4,6,7,11,13,15,24,31]

rotate(L,4)
print(L)