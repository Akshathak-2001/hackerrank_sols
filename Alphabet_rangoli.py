'''Alphabet rangoli:

You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
'''

import string

def print_rangoli(size):
    # your code goes here
    alp = list(string.ascii_lowercase)
    out_list = []
    width = (size *2 -1)* 2 - 1
    size_alp = alp[:size][::-1]
    for i in range(1, len(size_alp) + 1):
        half = "-".join(size_alp[0:i])
        half += half[:-1][::-1]
        out_list.append(half.center(width, "-"))
        
    out_list.extend(out_list[:-1][::-1])
    for output in out_list:
        print(output)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)