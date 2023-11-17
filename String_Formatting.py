'''Given an integer, n, print the following values for each integer i from 1 to n:

1.Decimal
2.Octal
3.Hexadecimal (capitalized)
4.Binary
'''

def print_formatted(number):
    width = len(f"{number:b}")
        
    for i in range(1, number+1):
        print(f'{i:>{width}} {i:>{width}o} {i:>{width}X} {i:>{width}b}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)