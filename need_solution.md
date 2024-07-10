1. You need to calculate the sum of the numbers in an array. However, the array contains nested arrays, whose numbers you must also count.  These nested arrays may also have further arrays recursively nested in them, and so on. You do not know how deep the nesting continues. If the list is empty, return zero.
    The arrays may also contain data that is not of the type number (strings, BigInts, objects, etc), which you should ignore.
    Examples
    nestedSum([1, 2, [3, [4], 5, "6"], 6]) // should == 21
    nestedSum([2, [[[[[3]]]]]]) // should == 5
    nestedSum([]) // should == 0

2. Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

3. Find unsorted array in array
4. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.