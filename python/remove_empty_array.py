def array_filter(array):
	for item in array: 
		if type(item) == list and not item :
			array.remove(item)
	return array


print(array_filter([1, 4, [1, 6, 1], [], [90, 12, 342], []]))

# Using built in method
print(list(filter(None,[[], 33, 34])))