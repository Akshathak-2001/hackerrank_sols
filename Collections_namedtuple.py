'''
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.

Your task is to help Dr. Wesley calculate the average marks of the students.
'''

from collections import namedtuple

st = int(input())
Student = namedtuple('Student', input())
total = 0
for _ in range(st):
    s = Student(*input().split())
    total += int(s.MARKS)
print(round(total/st, 2))