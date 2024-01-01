def list_conversion(lst):
  return { item: item for item in lst } # Dictionary comprehension

print(list_conversion([1, 2, 3]))
