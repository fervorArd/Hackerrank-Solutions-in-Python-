def swap_case(s):
    string = ''
    for i in s:
        if i.isupper():
            string = string + i.lower()
        else:
            string = string + i.upper()
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
