'''You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.

'''

n = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    commands = input().split()
    other_sets = set(map(int, input().split()))
    if commands[0] == "intersection_update":
        A.intersection_update(other_sets)
        
    if commands[0] == "update":
        A.update(other_sets)
        
    if commands[0] == "symmetric_difference_update":
        A.symmetric_difference_update(other_sets)
        
    if commands[0] == "difference_update":
        A.difference_update(other_sets)
print(sum(A))