'''You are given a function . You are also given  lists. The  list consists of  elements.

You have to pick one element from each list so that the value from the equation below is maximized:

%

 denotes the element picked from the  list . Find the maximized value  obtained.

 denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.
'''


from itertools import product

K, M = map(int ,input().split() )

box = []

for i in range(K):
    s = list(map(int, input().split(" ")))
    s.pop(0)
    box.append(s)
    

d = list(product(*box))

box2 = []
for i in d:
    box2.append(sum([x*x for x in i])%M)

print(max(box2))