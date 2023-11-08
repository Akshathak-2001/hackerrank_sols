'''#Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .S
'''


def minion_game(string):
    # your code goes here
    a="AEIOU"
    b=0
    c=0
    for i in range(len(string)):
        if not string[i] in a:
            b+=len(string)-i
        else:
            c+=len(string)-i      
    if b>c:
        print("Stuart", b)
    elif b<c:
        print("Kevin", c)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)