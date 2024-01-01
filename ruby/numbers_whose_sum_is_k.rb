def number_with_sum_k(array, k)
	numbers = {}
	result = []
	array.each do |number|
		diff = k - number 
		if numbers.key?(diff)
			result = [number, numbers[diff]]
			break
		else
			numbers[number] = number
		end
	end

	return result
end

puts number_with_sum_k([1, 3, 4,5 , 55], 56).inspect
