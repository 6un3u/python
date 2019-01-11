def plus(l):
    result = []
    for i in l :
        result.append(i + 1)
    return(result)
    
#input
num = input().split(' ')
l = list(map(int, num))

a = plus(l)
print(a)
