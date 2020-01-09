def print_formatted(number):
    wid = len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(wid)+' '+oct(i)[2:].rjust(wid)+' '+hex(i)[2:].upper().rjust(wid)+' '+bin(i)[2:].rjust(wid))
 
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
