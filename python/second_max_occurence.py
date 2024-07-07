# Develop a function that takes a string as input and identifies the longest palindromic substring within it.
# For instance, if the input string is 'babad', the function should return 'bab' as the longest palindromic substring.
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
