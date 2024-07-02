import sys

n = int(sys.stdin.readline().strip())
n_cards = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
m_cards = list(map(int, sys.stdin.readline().strip().split()))

n_dict = {}

for n in n_cards:
  if n in n_dict:
    n_dict[n] += 1
  else:
    n_dict[n] = 1

for m in m_cards:
  if m in n_dict:
    print(n_dict[m], end=' ')
  else:
     print(0, end=' ')