import sys
input = sys.stdin.readline

n = int(input())
cards_n = list(map(int,input().split()))
m = int(input())
cards_m = list(map(int,input().split()))

res = [0] * m

for i in range(m):
    if cards_m[i] in cards_n:
        res[i] += 1

print(*res)