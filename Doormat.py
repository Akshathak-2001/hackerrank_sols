'''Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be NXM. N( is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

'''

N = input()
num = list(map(int, N.split()))
row, col = num[0], num[1]
s = '.|.'

for r in range(1, row//2 + 1):
    c = s * (r*2 - 1)
    print(c.center(col, '-'))
    
print('WELCOME'.center(col, '-'))

for r in range(row//2, 0, -1):
    c = s * (r*2 - 1)
    print(c.center(col, '-'))