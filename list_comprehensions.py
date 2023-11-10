'''Let's learn about list comprehensions! You are given three integers, y and z representing the dimensions of a cuboid alongwith an integer n. Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i+j+k is not equalton. Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z Please use list comprehensions rather than multiple loops, as a learningexercise.

Example

x = 1

y = 1

z = 2

n = 3

Vie

All permutations of [i, j, k] are:

[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1), (1, 1, 2]].

Print an array of the elements that do not sum to n = 3

[ [0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]
'''


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n])