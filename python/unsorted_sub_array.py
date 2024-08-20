def find_unsorted_subarray(nums):
	n = len(nums)
    
	start, end = -1, -1
    
	for i in range(n - 1):
		if nums[i] > nums[i + 1]:
			start = i
			break
			
	if start == -1:
		return 0
    
	for j in range(n - 1, 0, -1):
		if nums[j] < nums[j - 1]:
			end = j
			break

	subarray_min = min(nums[start:end + 1])
	subarray_max = max(nums[start:end + 1])
    
	while start > 0 and nums[start - 1] > subarray_min:
		start -= 1
    
	while end < n - 1 and nums[end + 1] < subarray_max:
		end += 1
    
	return end - start + 1

nums = [2, 6, 10, 8, 4, 9, 15, 20]
length_of_unsorted = find_unsorted_subarray(nums)

print(f"The length of the unsorted subarray is: {length_of_unsorted}")
