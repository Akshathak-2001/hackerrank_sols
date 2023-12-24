'''
ABC is a right triangle,90' at B.
Therefore, <ABC = 90'.

Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find <MBC(angle 0', as shown in the figure) in degrees.

Input Format

The first line contains the length of side AB.
The second line contains the length of side BC.
'''

import math
ab = int(input())
bc = int(input())

ac = math.sqrt((ab**2) + (bc**2))

mc = ac/2

bca=math.asin(ab/ac) 
bm=math.sqrt((bc**2+mc**2)-(2*bc*mc*math.cos(bca))) 
mbc=math.asin(math.sin(bca)*mc/bm) 
print(int(round(math.degrees(mbc),0)),'\u00B0',sep="")