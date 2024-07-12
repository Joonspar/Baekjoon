import sys
import math
input = sys.stdin.readline

# 입력 받기
arr = []
while True:
    k = int(input())
    if k != 0:
        arr.append(k)
    else:
        break

# 에라토스테네스의 체를 사용하여 소수 구하기
max_k = max(arr)
max_val = 2 * max_k

is_prime = [True] * (max_val + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(math.sqrt(max_val)) + 1):
    if is_prime[i]:
        for j in range(i * i, max_val + 1, i):
            is_prime[j] = False

# 각 k에 대해 범위 (k, 2*k]의 소수 개수 세기
for elem in arr:
    cnt = 0
    for i in range(elem + 1, 2 * elem + 1):
        if is_prime[i]:
            cnt += 1
    print(cnt)
