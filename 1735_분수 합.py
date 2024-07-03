import math
import sys
input = sys.stdin.readline 
a_c , a_p = map(int,input().split())
b_c , b_p = map(int,input().split())

parent = math.lcm(a_p,b_p)
a1 = parent // a_p
b1 = parent // b_p

a_c *= a1
b_c *= b1
child = a_c + b_c

gcd = math.gcd(child,parent)
child //= gcd
parent //= gcd

print(child,parent)