'''
Consider the following:

*A string, s, of length n where s = c(0)c(1).....c(n-1).
*An integer, k, where k is a factor of n.

We can split s into n/k substrings where each subtring, t(i), consists of a contiguous block of k characters in s Then, use each t(i) to create string u(i) such that:

*The characters in u(i) are a subsequence of the characters in t(i).
*Any repeat occurrence of a character is removed from the string such that each character in u(i) occurs exactly once. In other words, if the character at some index j in t(i) occurs at a previous index <j in t(i), then do not include the character in string u(i).

Given s and k, print n/k lines where each line i denotes string u(i).
'''

import textwrap

def merge_the_tools(string, k):
    sub = textwrap.wrap(string,k)
    for s in sub:
        out =''
        for i in s:
            if i not in out:
                out = out + i
        print(out)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)