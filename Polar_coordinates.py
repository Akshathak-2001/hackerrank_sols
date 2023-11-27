'''
You are given a complex z. Your task is to convert it to polar coordinates.
'''

import cmath

z = complex(input())
print(cmath.polar(z)[0])
print(cmath.polar(z)[1])