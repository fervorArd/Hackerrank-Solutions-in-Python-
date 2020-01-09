def solve(s):
    fullName = ''
    nameList = s.split(' ')
    for i in nameList:
        if i=='':
            fullName += ' '
        else:
            fullName += i[0].upper()+i[1:len(i)]+' '
    return fullName
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
