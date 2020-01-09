list1 = input().split()
m = int(list1[0])
n = int(list1[1])
for i in range(m//2):
    print(('.|.'*i).rjust((n-3)//2,'-')+'.|.'+('.|.'*i).ljust((n-3)//2,'-'))
print('WELCOME'.center(n,'-'))
for i in range(m//2):
    print(('.|.'*(m//2-i-1)).rjust((n-3)//2,'-')+'.|.'+('.|.'*(m//2-i-1)).ljust((n-3)//2,'-'))
