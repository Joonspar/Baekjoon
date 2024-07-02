import math
T = int(input())

for _ in range(T):
    a,b = map(int,input().split())
    res = math.lcm(a,b)
    print(res)