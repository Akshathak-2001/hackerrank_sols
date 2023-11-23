'''Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
'''


from collections import Counter

X = int(input())
lst = list(map(int,input().split()))
N = int(input())
gain = 0
for i in range(N):
    xi = list(map(int,input().split()))
    if xi[0] in Counter(lst).keys():
        gain += xi[1]
        lst.remove(xi[0])

print(gain)