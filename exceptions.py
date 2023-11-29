'''You are given two values a and b.
Perform integer division and print a/b.
'''

for _ in range(int(input())):
    try:
        a, b = list(map(int, input().split()))
        try:
            print(int(a//b))
        except ZeroDivisionError as e:
            print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)