n,m = map(int,input().split())
n_set = set()
m_list = list()
for i in range(n):
    n_set.add(input())

for i in range(m):
    m_list.append(input())

cnt = 0

for i in m_list:
    if i in n_set:
        cnt += 1
print(cnt)