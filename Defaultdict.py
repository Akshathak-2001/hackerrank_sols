'''In this challenge, you will be given two integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.
'''

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(1, n+1):
    n_word = input()
    d[n_word].append(i)

for j in range(m):
    m_word = input()
    if d[m_word]:
        print(*d[m_word])
    else:
        print("-1")
