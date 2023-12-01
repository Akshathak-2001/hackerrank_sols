'''
ou are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.
'''

from collections import OrderedDict
n = int(input())
items = OrderedDict()
for i in range(n):
    item_name, net_price = input().rsplit(" ", 1)
    if item_name in items:
        items[item_name] += int(net_price)
    else:
        items[item_name] = int(net_price)
[print(i, items[i]) for i in items]