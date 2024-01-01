def max_product(array)
	max, second_max, third_max = 0

	array.each do |number|
		if number >= max
			third_max = second_max
			second_max = max
			max = number
		elsif number >= second_max
			third_max = second_max
			second_max = number
		elsif number >= third_max
			third_max = number
		end
	end
	return max * second_max * third_max
end

puts max_product([100, 2, 3 ,4 ,20, 20, 400])
