"""
Arrays & hashing - Anagram
An anagram is a word that when rearranged forms another word.

Some examples of anagram:

"listen" and "silent"
"cinema" and "iceman"
"Tom Marvolo Riddle" and "I am Lord Voldemort"

Key Approaches:
1. Sorting:
Time Complexity = O(n log n) due to the sorting operation, where n is the length of the strings.
Space Complexity = O(n) because strings are immutable and sorting creates new copies

2. Hash Map (Recommended):
3. Frequency Array:


"""
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))