def make_s(x):
	d = x % 10
	if x > 10:
		return d + make_s(int(x / 10))
	else:
		return d

n = input()

'''for check'''
a = 0
for i in n:
	a = a + int(i)
print(a)

n = int(n)
print(make_s(n))

