n,m = map(int,input().split())
cnt = 0
listen = []
see = []
res = []
for _ in range(n):
    listen.append(input())

for _ in range(m):
    see.append(input())

if n >= m:
    for elem in listen:
        if elem in see:
            cnt += 1
            res.append(elem)
else:
    for elem in see:
        if elem in listen:
            cnt += 1
            res.append(elem)
res.sort()
print(cnt)
for person in res:
    print(person)
