# Arrays $ Hashing - Contains duplicate items in an array

# It was solved using brute force nested loops approach.

num = [1, 2, 5, 4]

def duplicate(num):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] == num[j]:
                return True
    return False

print(duplicate(num))



"""
The following is the hash set approach

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
"""