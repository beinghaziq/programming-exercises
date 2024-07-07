# Please write a function that accepts a string as input and returns the second-highest occurring character in the string?
# For instance, if the input string is 'aaabbc', the function should return 'b' since 'b' occurs the second-highest number
# of times in the string.
def find_second_max_occurer(str):
    occurences = {}
    for letter in str:
        if letter in occurences:
            occurences[letter] += 1
        else:
            occurences[letter] = 1
    frequencies = list(occurences.values())
    frequencies.sort(reverse=True)
    sorted_list = frequencies[1]

    for key in occurences:
        if occurences[key] == sorted_list:
            return key


print(find_second_max_occurer("aaaaabbbbbcccccccccccdddddddddddddddddd"))
