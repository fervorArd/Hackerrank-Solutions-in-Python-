for _ in range(int(input())):
    print(input().replace(' && ', '%temp%').replace(' || ', ' or ').replace('%temp%', ' and ').replace(' && ', '%temp%').replace(' || ', ' or ').replace('%temp%', ' and '))
