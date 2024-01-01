def sum_of_numbers(numbers):
    array = []
    for x in numbers:
        array.append(get_digit_sum(str(x)))
    print(array)


def get_digit_sum(num):
    sum_of_digits = 0
    for x in num:
        sum_of_digits = sum_of_digits + int(x)
    return sum_of_digits
    
sum_of_numbers([21, 10])

# using list comprehension

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))


def array_of_sums(numbers):
    result = [sum_of_digits(x) for x in numbers]
    print(result)


array_of_sums([21, 10])
