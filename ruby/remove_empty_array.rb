def remove_empty_array(array)
	array.each do |item|
		array.delete(item) if item.is_a?(Array) && item.empty?
	end

		array
end

puts remove_empty_array([1, 4, [1, 6, 1], [], [90, 12, 342], []]).inspect

puts [1, 4, [1, 6, 1], [], [90, 12, 342], []].reject{ |i| i.is_a?(Array) && i.empty? }.inspect