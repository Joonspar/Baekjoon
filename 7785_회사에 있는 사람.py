n = int(input())

remain = {}
for _ in range(n):
    person , state = input().split()
    if state == 'enter':
        remain[person] = True
    if state == 'leave':
        remain[person] = False

res =  [i for i , j in remain.items() if j]

for elem in sorted(res,reverse=True):
    print(elem)