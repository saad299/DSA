'''
Arrays and Hashing - Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Key Approaches:
1. Brute Force:
Explanation: Use two nested loops to check every pair of indices (i, j) where i < j. If nums[i] + nums[j] equals the target, return [i, j].
Time Complexity: O(n²) due to the nested loops.
Space Complexity: O(1) as no extra space is used.

2. Hash Map (Recommended):
Explanation: Use a hash map to store previously seen values and their indices. For each element, calculate the complement (target - current value). If the complement exists in the hash map, return the current index and the stored index of the complement.
Time Complexity: O(n) as we only traverse the array once.
Space Complexity: O(n) for the hash map storage.

3. Brute Force: Uses nested loops to compare every pair of elements. It is simple but inefficient for large datasets.

4. Sorting + Two Pointers: Sorts the array first (O(nlogn)), then uses two pointers moving inward from both ends to find the pair. This requires additional logic to track original indices and is generally slower than the hash map approach for this specific problem.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer exists.

'''

# hash map approach
def twoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
    return []

# test
print(twoSum([2,7,11,15], 9)) # [0,1]
print(twoSum([3,2,4], 6)) # [1,2]
print(twoSum([3,3], 6)) # [0,1]
print(twoSum([1,2,3,4,5], 8)) # [2,4]
print(twoSum([1,2,3,4,5], 10)) # []

# brute force approach
def twoSum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# test
print(twoSum_brute_force([2,7,11,15], 9)) # [0,1]
print(twoSum_brute_force([3,2,4], 6)) # [1,2]
print(twoSum_brute_force([3,3], 6)) # [0,1]
print(twoSum_brute_force([1,2,3,4,5], 8)) # [2,4]
print(twoSum_brute_force([1,2,3,4,5], 10)) # []