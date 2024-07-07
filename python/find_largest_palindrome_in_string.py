# Develop a function that takes a string as input and identifies the longest palindromic substring within it.
# For instance, if the input string is 'babad', the function should return 'bab' as the longest palindromic substring.
def longest_palindromic_substring(s):
    start, end = 0, 0
    for i in range(len(s)):
        l1, r1 = expand_around_center(s, i, i)
        l2, r2 = expand_around_center(s, i, i + 1)

        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end]


def expand_around_center(s, left, right):
  while left >= 0 and right < len(s) and s[left] == s[right]:
    left -= 1
    right += 1
    return left + 1, right


input_string = 'babad'
print(longest_palindromic_substring(input_string))
