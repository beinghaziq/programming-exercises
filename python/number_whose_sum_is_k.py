def number_with_sum_k(array, k):
	numbers = {}
	result = []
	for number in array:
		diff = k - number 
		if diff in numbers:
			result = [number, numbers[diff]]
			break
		else:
			numbers[number] = number
	return result

print(number_with_sum_k([1, 3, 4,5 , 55], 56))
