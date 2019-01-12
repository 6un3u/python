def plus(l):
    result = []
    for i in l :
        result.append(i + 1)
    return(result)

# List Comprehension
def add_one(xs):
    return [x + 1 for x in xs]

# Use map with lambda
def add_one_map(xs):
    return map(lambda x: x + 1, xs)
    
#input
num = input().split(' ')
l = list(map(int, num))

a = plus(l)
print(a)
