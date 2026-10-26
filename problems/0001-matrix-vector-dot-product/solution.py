def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	lt=[]
	if len(a) == len(b):
		for i in range(len(a)):
			em=0
			for j in range(len(a[i])):
				em+=b[j]*a[i][j]
			lt.append(em)
		return lt
	else:
		return -1
	pass