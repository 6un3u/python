def find_even(xs):
	return [x for x in xs if x % 2 == 0]

# filter
def even(xs):
    return filter(lambda x: x % 2 == 0, xs)

l = [1, 2, 3, 4]
print(find_even(l))
