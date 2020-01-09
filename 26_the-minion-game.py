def minion_game(string):
    stuart = 0;kevin = 0
    for i in range(len(string)):
        if string[i] not in ['A','E','I','O','U','a','e','i','o','u']:
            stuart += (len(string)-i) 
        else:
            kevin += (len(string)-i) 
    if stuart>kevin:
        print('Stuart '+str(stuart)) 
    elif stuart<kevin:
        print('Kevin '+str(kevin))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
