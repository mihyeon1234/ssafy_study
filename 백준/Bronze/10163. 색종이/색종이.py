import sys

arr = [[0]*1001 for _ in range(1001)]

n = int(sys.stdin.readline())
for N in range(1, n+1):
    x, y, x1, y1 = map(int, sys.stdin.readline().split())
    for i in range(x, x+x1):
        for j in range(y, y+y1):
            arr[i][j] = N

for N in range(1, n+1):
    su = 0
    for co in range(1001):
        su += arr[co].count(N)
    print(su)