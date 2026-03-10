n = int(input())
rows = 2*n-1
star = n 
space = 0 

for i in range(1, rows + 1):
    for st in range(1,star+1):
        print('*',end='')
    for sp in range(1,space+1):
        print(' ',end='')
    for st in range(1,star+1):
        print('*',end='')
    print()
    if(i <= rows//2):
        star -= 1 
        space += 2
    else:
        star += 1 
        space -= 2
