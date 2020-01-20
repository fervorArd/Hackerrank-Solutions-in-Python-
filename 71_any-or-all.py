N, num_list = int(input()),list(map(int,input().split()))
print(all((x>0) for x in num_list) and any(str(x)[-1:]==str(x) for x in num_list))
