def is_square(n):
	if n != 0:
		x = n // 2
	y = set([x])
	while x*x != n and x != 0:
		x = (x + (n // x)) // 2
		if x in y: return False
		y.add(x)
	return True
	
# map() = [F(x) for x in L]
# filter() = [x for x in L if F]
def list_squared(m,n):
	inputs = list(range(m, n+1))
	numbers = [list(range(1, x+1)) for x in inputs]
	for i in inputs:
		for j in numbers:
			divisors = [x for x in j if i%x == 0]
		squares = [x*x for x in divisors] # square, sum, return with inputs if sum is a square
		if is_square(sum(squares)):
			print([i, sum(squares)])
		
	
list_squared(1, 250)
