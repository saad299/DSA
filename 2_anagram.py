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

-->Pros
Simplicity: It is easy to understand and implement, requiring only a sort function and an equality check.
Low Memory Overhead: It typically requires less auxiliary space than hash-based methods, as it does not need to store frequency maps or dictionaries.

-->Cons
Higher Time Complexity: Sorting takes O(n log n) time (or O(n log n + m log m) for two strings), which is significantly slower than the O(n + m) linear time achieved by hash table or frequency array methods. 
Inefficiency for Large Inputs: The performance bottleneck of sorting becomes problematic with long strings or large datasets, making it suboptimal compared to counting-based approaches.

2. Hash Map (Recommended):
Time Complexity: O(n)
Space Complexity: O(k)

3. Frequency Array:


"""
# Sorting method
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))

# Hash Map method:
def isAnagramHashMap(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT

print(isAnagramHashMap("anagram", "nagaram"))
print(isAnagramHashMap("rat", "car"))