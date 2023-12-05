'''
You have a non-empty set s, and you have to execute N commands given in N lines.

The commands will be pop, remove and discard.
'''
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(0,N):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        if len(command) == 2:
            element = int(command[1])
            if element in s:
                s.remove(element)
    elif command[0] == 'discard':
        if len(command) == 2:
            element = int(command[1])
            s.discard(element)

print(sum(s))