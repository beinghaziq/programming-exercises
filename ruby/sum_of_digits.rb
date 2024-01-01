def sum_of_numbers(numbers)
    puts numbers.map { |num| num.digits.sum }.inspect
end
    
sum_of_numbers([21, 160])
