def power(x, n):
	s = 1
	while(n > 0):
		s = s * x
		n = n-1
	return s