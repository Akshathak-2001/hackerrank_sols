'''You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
'''

from itertools import combinations
lst = list(input().split())
s = lst[0]
k = lst[1]
for j in range(1,int(k)+1):
    for i in combinations(sorted(s),j):
        print(''.join(i))