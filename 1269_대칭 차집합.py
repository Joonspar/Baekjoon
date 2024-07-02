n,m = map(int,input().split())
A =set(map(int,input().split()))
B = set(map(int,input().split()))

diff1 = A - B
diff2 = B - A

print(len(diff1) + len(diff2) - 2)