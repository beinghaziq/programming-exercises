from itertools import permutations
def possible_combinations(array):
    for i in array:
        for j in array:
            for k in array:
                if i != j and j != k and k != i:
                  print(i, j, k)


possible_combinations([3, 6, 9])


# Using builtin methods
print(list(permutations([1, 2, 4], 3)))