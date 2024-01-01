def array_to_hash(array)
    hash = {}
    array.each do |item|
        hash[item] = item
    end

    return hash
end

puts array_to_hash([1, 2, 3])

puts [1, 2, 3].to_h { |item| [item, item] }