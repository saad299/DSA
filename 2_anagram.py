"""
Arrays & hashing - Anagram
An anagram is a word that when rearranged forms another word.

Some examples of anagram:

"listen" and "silent"
"cinema" and "iceman"
"Tom Marvolo Riddle" and "I am Lord Voldemort"

Key Approaches:
1. Sorting:
Explanation: Sort both strings and compare the sorted results. If they are identical, the strings are anagrams.
Time Complexity = O(n log n) due to the sorting operation, where n is the length of the strings.
Space Complexity = O(n) because strings are immutable and sorting creates new copies

-->Pros
Simplicity: It is easy to understand and implement, requiring only a sort function and an equality check.
Low Memory Overhead: It typically requires less auxiliary space than hash-based methods, as it does not need to store frequency maps or dictionaries.

-->Cons
Higher Time Complexity: Sorting takes O(n log n) time (or O(n log n + m log m) for two strings), which is significantly slower than the O(n + m) linear time achieved by hash table or frequency array methods. 
Inefficiency for Large Inputs: The performance bottleneck of sorting becomes problematic with long strings or large datasets, making it suboptimal compared to counting-based approaches.

2. Hash Map (Recommended):
Explanation: Count the frequency of each character in both strings using a hash map (dictionary). If the frequency maps are identical, the strings are anagrams.
Time Complexity: O(n)
Space Complexity: O(k)

-->Pros
Linear Time Complexity: Hash map operations (insertion and lookup) are O(1) on average, making the overall time complexity O(n), which is much faster than sorting.
Scalability: This method scales well with larger inputs, as the linear time complexity is more efficient than the O(n log n) complexity of sorting.

-->Cons
Higher Space Complexity: Hash maps require additional space to store the frequency counts, leading to a space complexity of O(k), where k is the number of unique characters.

3. Frequency Array:
Explanation: Use a fixed-size array (for lowercase English letters, size 26) to count character frequencies. Increment for characters in the first string and decrement for characters in the second string. If all counts are zero, the strings are anagrams.
Time Complexity: O(n)
Space Complexity: O(1) - fixed size array of 26 characters

-->Pros
Constant Space Complexity: Uses a fixed-size array, making it very memory efficient.
Fast Execution: Direct array indexing provides quick access and updates.

-->Cons
Limited to Specific Character Sets: Only works reliably for strings with a limited, known character set (e.g., lowercase English letters). For Unicode or larger character sets, this method becomes impractical.
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

# Frequency Array method:
def isAnagramFrequencyArray(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    return count == [0] * 26

print(isAnagramFrequencyArray("anagram", "nagaram"))
print(isAnagramFrequencyArray("rat", "car"))