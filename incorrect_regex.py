'''
You are given a string S.
Your task is to find out whether S is a valid regex or not.

ps: works in Pypy3
'''

import re

T = int(input())
for i in range(T):
    reg = input()
    try:
        re.compile(reg)
        print(True)
    except re.error:
        print(False)
