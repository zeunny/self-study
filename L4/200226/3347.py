import sys

sys.stdin = open('3347.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    result = [0]*N

    for i in range(M):
        for j in range(N):
            if B[i] >= A[j]:
                result[j] += 1
                break

    print(f'#{tc} {result.index(max(result))+1}')