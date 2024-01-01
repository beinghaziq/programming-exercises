def max_product(array):
	maximum, second_max, third_max = [0, 0, 0]

	for number in array:
		if number >= maximum:
			third_max = second_max
			second_max = maximum
			maximum = number
		elif number >= second_max:
			third_max = second_max
			second_max = number
		elif number >= third_max:
			third_max = number

	return maximum * second_max * third_max

print(max_product([100, 2, 3 ,4 ,20, 20, 400]))
