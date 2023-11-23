'''You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
'''

from itertools import permutations
lst = list(input().split())
s = lst[0]
k = lst[1]
out = sorted(permutations(s,int(k)))

for i in out:
    print((*i), sep = '') 