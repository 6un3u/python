'''map 함수 사용'''

def plus(l):
	return l + 1

#input	
num = input().split(' ')
l = list(map(int, num))

a = list(map(plus, l))
print(a)

