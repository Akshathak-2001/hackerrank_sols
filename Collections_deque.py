'''
Perform append, pop, popleft and appendleft methods on an empty deque d.
'''

from collections import deque
N = int(input())
d = deque()
for _ in range(N):
    method = input().split()
    if len(method) == 1:
        eval(f"d.{method[0]}()")
    else:
        eval(f"d.{method[0]}({method[1]})")
print(*d)