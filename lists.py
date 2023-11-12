'''Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''

if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        s = list(input().split())
        if s[0]=='insert':
            lst.insert(int(s[1]), int(s[2]))
        if s[0]=='remove':
            lst.remove(int(s[1]))
        if s[0]=='append':
            lst.append(int(s[1]))
        if s[0]=='sort':
            lst.sort()
        if s[0]=='pop':
            lst.pop()
        if s[0]=='reverse':
            lst.reverse()
        if s[0]=='print':
            print(lst)