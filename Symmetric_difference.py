'''
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
'''


m, a = int(input()), set(map(int, input().split()))
n, b = int(input()), set(map(int, input().split()))
[print(i) for i in sorted(b.symmetric_difference(a))]