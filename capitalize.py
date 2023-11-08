#ensure that the first and last names of people begin with a capital letter in their passports. 

def solve(s):
    words = s.split(' ')
    ret = []
    for i in words:
        ret.append(i.capitalize())
    return ' '.join(ret)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()