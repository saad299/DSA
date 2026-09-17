# DSA 150 — Full Problem Set, Ordered by Difficulty

Each problem below has a short task description (written from scratch, not copied from LeetCode) so you can read it and start coding directly in your editor. Difficulty and examples are illustrative — LeetCode's official test cases will have more edge cases, so once you think you've solved it, paste your solution into LeetCode (search the exact name) to confirm against their full test suite before committing as "done."

---

## 🟢 EASY (28 problems)

### 1. Contains Duplicate — *Arrays & Hashing*
Given an array of integers, return `true` if any value appears at least twice, `false` if all values are distinct.
**Example:** `[1,2,3,1]` → `true` | `[1,2,3,4]` → `false`

### 2. Valid Anagram — *Arrays & Hashing*
Given two strings, return `true` if the second is an anagram of the first (same letters, same frequency, different order allowed).
**Example:** `"anagram"`, `"nagaram"` → `true`

### 3. Two Sum — *Arrays & Hashing*
Given an array of integers and a target number, return the indices of the two numbers that add up to the target. Assume exactly one solution exists.
**Example:** `[2,7,11,15]`, target `9` → `[0,1]`

### 4. Valid Palindrome — *Two Pointers*
Given a string, determine if it reads the same forward and backward after ignoring non-alphanumeric characters and case.
**Example:** `"A man, a plan, a canal: Panama"` → `true`

### 5. Best Time to Buy and Sell Stock — *Sliding Window*
Given an array where each element is a stock price on that day, find the maximum profit from buying on one day and selling on a later day. Return 0 if no profit is possible.
**Example:** `[7,1,5,3,6,4]` → `5` (buy at 1, sell at 6)

### 6. Valid Parentheses — *Stack*
Given a string containing only `(){}[]`, determine if the brackets are properly closed and nested in the correct order.
**Example:** `"()[]{}"` → `true` | `"(]"` → `false`

### 7. Binary Search — *Binary Search*
Given a sorted array of integers and a target, return the index of the target if found, else `-1`. Must run in O(log n).
**Example:** `[-1,0,3,5,9,12]`, target `9` → `4`

### 8. Reverse Linked List — *Linked List*
Given the head of a singly linked list, reverse it and return the new head.
**Example:** `1→2→3→4→5` → `5→4→3→2→1`

### 9. Merge Two Sorted Lists — *Linked List*
Given the heads of two sorted linked lists, merge them into one sorted list and return its head.
**Example:** `1→2→4` and `1→3→4` → `1→1→2→3→4→4`

### 10. Linked List Cycle — *Linked List*
Given the head of a linked list, determine if it contains a cycle (a node's next pointer eventually loops back to a previous node).

### 11. Invert Binary Tree — *Trees*
Given the root of a binary tree, swap every left and right child recursively and return the new root.

### 12. Maximum Depth of Binary Tree — *Trees*
Given the root of a binary tree, return the number of nodes along the longest path from root to the farthest leaf.

### 13. Diameter of Binary Tree — *Trees*
Given the root of a binary tree, return the length (in edges) of the longest path between any two nodes — the path may or may not pass through the root.

### 14. Balanced Binary Tree — *Trees*
Given the root of a binary tree, determine if it's height-balanced (the left and right subtree heights of every node differ by no more than 1).

### 15. Same Tree — *Trees*
Given the roots of two binary trees, determine if they are structurally identical with the same node values.

### 16. Subtree of Another Tree — *Trees*
Given the roots of two binary trees, determine if the second tree is a subtree of the first (a node in the first tree with the exact same structure and values as the root of the second).

### 17. Kth Largest Element in a Stream — *Heap / Priority Queue*
Design a class that, given a stream of integers added one at a time, always returns the k-th largest element seen so far.

### 18. Last Stone Weight — *Heap / Priority Queue*
Given an array of stone weights, repeatedly smash the two heaviest stones together (if equal, both destroyed; if not, the difference remains) until at most one stone is left. Return that stone's weight, or 0 if none remain.
**Example:** `[2,7,4,1,8,1]` → `1`

### 19. Climbing Stairs — *1-D Dynamic Programming*
Given `n` stairs, where you can climb 1 or 2 steps at a time, return how many distinct ways you can reach the top.
**Example:** `n=3` → `3` (1+1+1, 1+2, 2+1)

### 20. Min Cost Climbing Stairs — *1-D Dynamic Programming*
Given an array where each index has a cost, and you can start from index 0 or 1 and climb 1 or 2 steps at a time, find the minimum cost to reach the top (past the last index).

### 21. Meeting Rooms — *Intervals*
Given an array of meeting time intervals, determine if a single person can attend all of them (i.e., no two intervals overlap).
**Example:** `[[0,30],[5,10],[15,20]]` → `false`

### 22. Happy Number — *Math & Geometry*
A number is "happy" if repeatedly replacing it with the sum of the squares of its digits eventually reaches 1. Given a number, return whether it's happy.
**Example:** `19` → `true` (1²+9²=82 → 8²+2²=68 → 6²+8²=100 → 1²+0²+0²=1)

### 23. Plus One — *Math & Geometry*
Given an array of digits representing a non-negative integer (most significant digit first), add one to the number and return the result as a digit array.
**Example:** `[1,2,3]` → `[1,2,4]` | `[9,9]` → `[1,0,0]`

### 24. Single Number — *Bit Manipulation*
Given an array where every element appears twice except one, find the one that appears only once. Must run in O(n) time with O(1) extra space.
**Example:** `[4,1,2,1,2]` → `4`

### 25. Number of 1 Bits — *Bit Manipulation*
Given an unsigned integer, return the number of `1` bits in its binary representation.
**Example:** `11 (binary 1011)` → `3`

### 26. Counting Bits — *Bit Manipulation*
Given an integer `n`, return an array where each index `i` (from 0 to n) holds the count of `1` bits in the binary representation of `i`.
**Example:** `n=2` → `[0,1,1]`

### 27. Reverse Bits — *Bit Manipulation*
Given a 32-bit unsigned integer, reverse its bits and return the resulting integer.

### 28. Missing Number — *Bit Manipulation*
Given an array containing `n` distinct numbers from the range `0` to `n`, find the one number missing from the range.
**Example:** `[3,0,1]` → `2`

---

## 🟡 MEDIUM (101 problems)

### 29. Group Anagrams — *Arrays & Hashing*
Given an array of strings, group all anagrams together and return the groups (order of groups/elements doesn't matter).
**Example:** `["eat","tea","tan","ate","nat","bat"]` → `[["eat","tea","ate"],["tan","nat"],["bat"]]`

### 30. Top K Frequent Elements — *Arrays & Hashing*
Given an array of integers and an integer `k`, return the `k` most frequently occurring elements.
**Example:** `[1,1,1,2,2,3]`, k=`2` → `[1,2]`

### 31. Product of Array Except Self — *Arrays & Hashing*
Given an array, return a new array where each index holds the product of all other elements except itself, without using division and in O(n).
**Example:** `[1,2,3,4]` → `[24,12,8,6]`

### 32. Valid Sudoku — *Arrays & Hashing*
Given a partially filled 9x9 Sudoku board, determine if the currently filled cells satisfy Sudoku rules (no repeated digit 1-9 in any row, column, or 3x3 box). You don't need to check if it's solvable.

### 33. Encode and Decode Strings — *Arrays & Hashing*
Design an algorithm to encode a list of strings into a single string, and decode it back into the original list of strings, handling strings that may contain any characters (including delimiters).

### 34. Longest Consecutive Sequence — *Arrays & Hashing*
Given an unsorted array of integers, find the length of the longest run of consecutive integers (they don't need to be in order in the array). Must run in O(n).
**Example:** `[100,4,200,1,3,2]` → `4` (1,2,3,4)

### 35. Two Sum II - Input Array Is Sorted — *Two Pointers*
Given a 1-indexed sorted array and a target, return the indices of two numbers that add up to the target, using O(1) extra space.

### 36. 3Sum — *Two Pointers*
Given an array of integers, find all unique triplets that sum to zero.
**Example:** `[-1,0,1,2,-1,-4]` → `[[-1,-1,2],[-1,0,1]]`

### 37. Container With Most Water — *Two Pointers*
Given an array of heights representing vertical lines, find two lines that together with the x-axis form a container holding the most water.
**Example:** `[1,8,6,2,5,4,8,3,7]` → `49`

### 38. Longest Substring Without Repeating Characters — *Sliding Window*
Given a string, find the length of the longest substring without repeating characters.
**Example:** `"abcabcbb"` → `3` ("abc")

### 39. Longest Repeating Character Replacement — *Sliding Window*
Given a string and an integer `k`, find the length of the longest substring you can get containing the same letter after replacing at most `k` characters.
**Example:** `"AABABBA"`, k=`1` → `4`

### 40. Permutation in String — *Sliding Window*
Given two strings, determine if the second contains a permutation (rearrangement) of the first as a contiguous substring.
**Example:** `s1="ab"`, `s2="eidbaooo"` → `true` ("ba" is a permutation of "ab")

### 41. Min Stack — *Stack*
Design a stack that supports push, pop, top, and retrieving the minimum element — all in O(1) time.

### 42. Evaluate Reverse Polish Notation — *Stack*
Given an array of tokens representing an arithmetic expression in Reverse Polish (postfix) Notation, evaluate it and return the result.
**Example:** `["2","1","+","3","*"]` → `9`

### 43. Generate Parentheses — *Stack*
Given `n` pairs of parentheses, generate all combinations of well-formed (properly nested and balanced) parentheses.
**Example:** `n=3` → `["((()))","(()())","(())()","()(())","()()()"]`

### 44. Daily Temperatures — *Stack*
Given an array of daily temperatures, return an array where each index holds how many days you'd have to wait for a warmer temperature (0 if none exists).
**Example:** `[73,74,75,71,69,72,76,73]` → `[1,1,4,2,1,1,0,0]`

### 45. Car Fleet — *Stack*
Given positions and speeds of cars heading to the same destination on a one-lane road, determine how many "fleets" (groups that arrive together, since faster cars catch up but can't pass) will arrive.

### 46. Search a 2D Matrix — *Binary Search*
Given an m×n matrix where each row is sorted and the first integer of each row is greater than the last integer of the previous row, determine if a target value exists, in O(log(m*n)).

### 47. Koko Eating Bananas — *Binary Search*
Given piles of bananas and `h` hours to eat them all (Koko eats at a constant speed of `k` bananas/hour per pile, finishing a pile before starting the next in that hour), find the minimum eating speed `k` so all bananas are eaten within `h` hours.

### 48. Find Minimum in Rotated Sorted Array — *Binary Search*
Given a sorted array that's been rotated at some unknown pivot, find the minimum element in O(log n).
**Example:** `[4,5,6,7,0,1,2]` → `0`

### 49. Search in Rotated Sorted Array — *Binary Search*
Given a rotated sorted array and a target, return its index (or -1 if not found), in O(log n).

### 50. Time Based Key-Value Store — *Binary Search*
Design a key-value store that supports storing multiple values for the same key at different timestamps, and retrieving the value for a key at (or just before) a given timestamp.

### 51. Reorder List — *Linked List*
Given a singly linked list `L0→L1→...→Ln`, reorder it in-place to `L0→Ln→L1→Ln-1→L2→Ln-2→...`

### 52. Remove Nth Node From End of List — *Linked List*
Given the head of a linked list, remove the n-th node from the end and return the head, ideally in one pass.

### 53. Copy List with Random Pointer — *Linked List*
Given a linked list where each node has a `next` pointer and a `random` pointer (pointing to any node or null), create a deep copy of the list.

### 54. Add Two Numbers — *Linked List*
Given two non-empty linked lists representing two non-negative integers in reverse digit order, add them and return the sum as a linked list in the same format.
**Example:** `2→4→3` (342) + `5→6→4` (465) → `7→0→8` (807)

### 55. Find the Duplicate Number — *Linked List*
Given an array of `n+1` integers where each is between 1 and `n`, find the one duplicate number, without modifying the array and using O(1) extra space.

### 56. LRU Cache — *Linked List*
Design a Least Recently Used cache with `get` and `put` operations, both running in O(1), evicting the least recently used item when capacity is exceeded.

### 57. Lowest Common Ancestor of a Binary Search Tree — *Trees*
Given a BST and two nodes, find their lowest common ancestor (the deepest node that has both as descendants).

### 58. Binary Tree Level Order Traversal — *Trees*
Given the root of a binary tree, return the values of nodes grouped level by level (top to bottom, left to right within each level).

### 59. Binary Tree Right Side View — *Trees*
Given the root of a binary tree, return the values visible when viewing the tree from the right side, top to bottom.

### 60. Count Good Nodes in Binary Tree — *Trees*
Given a binary tree, a node is "good" if the path from the root to it contains no value greater than the node's own value. Count all good nodes.

### 61. Validate Binary Search Tree — *Trees*
Given the root of a binary tree, determine if it's a valid BST (left subtree values < node < right subtree values, recursively).

### 62. Kth Smallest Element in a BST — *Trees*
Given the root of a BST and an integer `k`, find the k-th smallest value in it.

### 63. Construct Binary Tree from Preorder and Inorder Traversal — *Trees*
Given two integer arrays representing preorder and inorder traversal of a binary tree, reconstruct and return the tree.

### 64. Implement Trie (Prefix Tree) — *Tries*
Design a Trie with `insert`, `search` (exact word match), and `startsWith` (prefix match) operations.

### 65. Design Add and Search Words Data Structure — *Tries*
Design a data structure supporting adding words and searching for a word, where the search may include `.` as a wildcard matching any single letter.

### 66. K Closest Points to Origin — *Heap / Priority Queue*
Given an array of points on a 2D plane and an integer `k`, return the `k` points closest to the origin (0,0).

### 67. Kth Largest Element in an Array — *Heap / Priority Queue*
Given an unsorted array and an integer `k`, find the k-th largest element (not the k-th distinct element).
**Example:** `[3,2,1,5,6,4]`, k=`2` → `5`

### 68. Task Scheduler — *Heap / Priority Queue*
Given a list of tasks (represented by letters) and a cooldown period `n` between two same tasks, find the minimum number of time units (including idle slots) needed to complete all tasks.

### 69. Design Twitter — *Heap / Priority Queue*
Design a simplified Twitter where users can post tweets, follow/unfollow others, and see the 10 most recent tweets in their news feed (own + followed users').

### 70. Subsets — *Backtracking*
Given an array of unique integers, return all possible subsets (the power set).
**Example:** `[1,2,3]` → `[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]`

### 71. Combination Sum — *Backtracking*
Given an array of distinct positive integers and a target, return all unique combinations where the numbers (reusable unlimited times) sum to the target.

### 72. Permutations — *Backtracking*
Given an array of distinct integers, return all possible permutations (orderings).
**Example:** `[1,2,3]` → `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

### 73. Subsets II — *Backtracking*
Given an array of integers that may contain duplicates, return all possible unique subsets.

### 74. Combination Sum II — *Backtracking*
Given an array of integers (may contain duplicates) and a target, find all unique combinations where numbers (each used only once) sum to the target.

### 75. Word Search — *Backtracking*
Given a 2D grid of letters and a word, determine if the word can be formed by tracing a path of adjacent cells (horizontally/vertically, no cell reused).

### 76. Palindrome Partitioning — *Backtracking*
Given a string, partition it such that every substring in the partition is a palindrome. Return all possible partitions.

### 77. Letter Combinations of a Phone Number — *Backtracking*
Given a string of digits (2-9), return all possible letter combinations the digits could represent based on a standard phone keypad mapping.

### 78. Number of Islands — *Graphs*
Given a 2D grid of `1`s (land) and `0`s (water), count the number of islands (connected groups of `1`s, horizontally/vertically adjacent).

### 79. Max Area of Island — *Graphs*
Given a 2D grid of `0`s and `1`s, find the maximum area (cell count) of any island.

### 80. Clone Graph — *Graphs*
Given a reference to a node in a connected undirected graph, return a deep copy (clone) of the entire graph.

### 81. Walls and Gates — *Graphs*
Given a 2D grid with walls, gates, and empty rooms, fill each empty room with the distance to its nearest gate.

### 82. Rotting Oranges — *Graphs*
Given a grid where cells are empty, fresh oranges, or rotten oranges, and every minute a rotten orange rots its fresh neighbors, find the minimum minutes until no fresh orange remains (or -1 if impossible).

### 83. Pacific Atlantic Water Flow — *Graphs*
Given a grid of heights representing a landscape bordered by the Pacific (top/left) and Atlantic (bottom/right) oceans, find all cells from which water can flow to both oceans (water flows to equal or lower height neighbors).

### 84. Surrounded Regions — *Graphs*
Given a 2D board of `X`s and `O`s, capture (flip to `X`) all regions of `O`s that are completely surrounded by `X`s (regions touching the border are safe).

### 85. Course Schedule — *Graphs*
Given a number of courses and a list of prerequisite pairs, determine if it's possible to finish all courses (i.e., no circular dependency).

### 86. Course Schedule II — *Graphs*
Same setup as Course Schedule, but return a valid order to take all courses, or an empty array if impossible.

### 87. Graph Valid Tree — *Graphs*
Given `n` nodes and a list of edges, determine if the edges form a valid tree (connected, no cycles).

### 88. Number of Connected Components in an Undirected Graph — *Graphs*
Given `n` nodes and a list of undirected edges, return the number of connected components.

### 89. Redundant Connection — *Graphs*
Given a graph that started as a tree but has one extra edge added (creating exactly one cycle), find that redundant edge.

### 90. Min Cost to Connect All Points — *Advanced Graphs*
Given points on a 2D plane, find the minimum total cost to connect all points, where the cost between two points is their Manhattan distance (essentially: build a Minimum Spanning Tree).

### 91. Network Delay Time — *Advanced Graphs*
Given a network of nodes with weighted directed edges (travel times) and a starting node, find the time it takes for a signal to reach all nodes (or -1 if impossible).

### 92. Cheapest Flights Within K Stops — *Advanced Graphs*
Given flights with costs between cities, find the cheapest price from a source to a destination city with at most `k` stops along the way.

### 93. House Robber — *1-D Dynamic Programming*
Given an array representing money in houses along a street, find the maximum amount you can rob without robbing two adjacent houses.
**Example:** `[1,2,3,1]` → `4` (rob house 1 and 3)

### 94. House Robber II — *1-D Dynamic Programming*
Same as House Robber, but the houses are arranged in a circle (first and last are adjacent).

### 95. Longest Palindromic Substring — *1-D Dynamic Programming*
Given a string, find the longest substring that is a palindrome.
**Example:** `"babad"` → `"bab"` or `"aba"`

### 96. Palindromic Substrings — *1-D Dynamic Programming*
Given a string, count how many substrings (including single characters) are palindromes.

### 97. Decode Ways — *1-D Dynamic Programming*
Given a string of digits where `'A'=1` ... `'Z'=26`, count the number of ways it can be decoded into letters.
**Example:** `"226"` → `3` ("BZ", "VF", "BBF")

### 98. Coin Change — *1-D Dynamic Programming*
Given coin denominations and a target amount, find the minimum number of coins needed to make that amount (or -1 if impossible).
**Example:** `coins=[1,2,5]`, amount=`11` → `3` (5+5+1)

### 99. Maximum Product Subarray — *1-D Dynamic Programming*
Given an array of integers, find the contiguous subarray with the largest product.

### 100. Word Break — *1-D Dynamic Programming*
Given a string and a dictionary of words, determine if the string can be segmented into a sequence of one or more dictionary words.
**Example:** `s="leetcode"`, dict=`["leet","code"]` → `true`

### 101. Longest Increasing Subsequence — *1-D Dynamic Programming*
Given an array of integers, find the length of the longest strictly increasing subsequence.
**Example:** `[10,9,2,5,3,7,101,18]` → `4` (2,3,7,101)

### 102. Partition Equal Subset Sum — *1-D Dynamic Programming*
Given an array of positive integers, determine if it can be split into two subsets with equal sums.

### 103. Unique Paths — *2-D Dynamic Programming*
Given an m×n grid, find how many unique paths exist from the top-left to bottom-right corner, only moving right or down.

### 104. Longest Common Subsequence — *2-D Dynamic Programming*
Given two strings, find the length of their longest common subsequence (not necessarily contiguous, but order-preserved).
**Example:** `"abcde"`, `"ace"` → `3`

### 105. Best Time to Buy and Sell Stock with Cooldown — *2-D Dynamic Programming*
Given stock prices per day, maximize profit with unlimited transactions, but after selling you must wait one day (cooldown) before buying again.

### 106. Coin Change II — *2-D Dynamic Programming*
Given coin denominations and a target amount, find the number of distinct combinations (order doesn't matter) that make up that amount.

### 107. Target Sum — *2-D Dynamic Programming*
Given an array of integers and a target, count the number of ways to assign `+` or `-` in front of each number so the expression equals the target.

### 108. Interleaving String — *2-D Dynamic Programming*
Given three strings, determine if the third can be formed by interleaving the first two while preserving each one's relative character order.

### 109. Edit Distance — *2-D Dynamic Programming*
Given two strings, find the minimum number of operations (insert, delete, replace) needed to convert one into the other.
**Example:** `"horse"` → `"ros"` → `3`

### 110. Maximum Subarray — *Greedy*
Given an array of integers, find the contiguous subarray with the largest sum.
**Example:** `[-2,1,-3,4,-1,2,1,-5,4]` → `6` (4,-1,2,1)

### 111. Jump Game — *Greedy*
Given an array where each element is the max jump length from that position, determine if you can reach the last index starting from index 0.

### 112. Jump Game II — *Greedy*
Same setup as Jump Game, but find the minimum number of jumps needed to reach the last index (assume it's always reachable).

### 113. Gas Station — *Greedy*
Given gas amounts and costs to travel between stations arranged in a circle, determine the starting station index from which you can complete the full circuit (or -1 if impossible).

### 114. Hand of Straights — *Greedy*
Given a hand of cards and a group size `w`, determine if the cards can be rearranged into groups of `w` consecutive cards each.

### 115. Merge Triplets to Form Target Triplet — *Greedy*
Given an array of triplets and a target triplet, determine if you can select some triplets and merge them (taking max of each position) to exactly form the target.

### 116. Partition Labels — *Greedy*
Given a string, partition it into as many parts as possible so each letter appears in only one part; return the sizes of these parts.
**Example:** `"ababcbacadefegdehijhklij"` → `[9,7,8]`

### 117. Valid Parenthesis String — *Greedy*
Given a string containing `(`, `)`, and `*` (which can be treated as `(`, `)`, or empty), determine if the string could be a valid parentheses sequence.

### 118. Insert Interval — *Intervals*
Given a set of non-overlapping intervals sorted by start time, insert a new interval, merging if necessary, and return the updated set.

### 119. Merge Intervals — *Intervals*
Given an array of intervals, merge all overlapping intervals and return the resulting non-overlapping set.
**Example:** `[[1,3],[2,6],[8,10],[15,18]]` → `[[1,6],[8,10],[15,18]]`

### 120. Non-overlapping Intervals — *Intervals*
Given an array of intervals, find the minimum number you'd need to remove to make the rest non-overlapping.

### 121. Meeting Rooms II — *Intervals*
Given an array of meeting intervals, find the minimum number of conference rooms required to hold all meetings.

### 122. Rotate Image — *Math & Geometry*
Given an n×n matrix representing an image, rotate it 90 degrees clockwise, in-place.

### 123. Spiral Matrix — *Math & Geometry*
Given an m×n matrix, return all its elements in spiral order (clockwise, starting top-left).

### 124. Set Matrix Zeroes — *Math & Geometry*
Given an m×n matrix, if an element is 0, set its entire row and column to 0, in-place.

### 125. Pow(x, n) — *Math & Geometry*
Implement `pow(x, n)`, computing `x` raised to the power `n`, efficiently (better than O(n) multiplications).

### 126. Multiply Strings — *Math & Geometry*
Given two numbers represented as strings, return their product as a string, without converting them directly to integers.

### 127. Detect Squares — *Math & Geometry*
Design a data structure that adds points and can count how many axis-aligned squares can be formed using a given point and previously added points.

### 128. Sum of Two Integers — *Bit Manipulation*
Given two integers, calculate their sum without using the `+` or `-` operators (use bitwise operations).

### 129. Reverse Integer — *Bit Manipulation*
Given a signed 32-bit integer, reverse its digits. Return 0 if the reversed value overflows the 32-bit signed integer range.
**Example:** `123` → `321` | `-123` → `-321`

---

## 🔴 HARD (20 problems)

### 130. Trapping Rain Water — *Two Pointers*
Given an array representing an elevation map, compute how much rainwater it can trap after raining.
**Example:** `[0,1,0,2,1,0,1,3,2,1,2,1]` → `6`

### 131. Minimum Window Substring — *Sliding Window*
Given two strings `s` and `t`, find the smallest substring of `s` that contains every character of `t` (including duplicates).
**Example:** `s="ADOBECODEBANC"`, `t="ABC"` → `"BANC"`

### 132. Sliding Window Maximum — *Sliding Window*
Given an array and a window size `k`, return the maximum value in each sliding window as it moves across the array.

### 133. Largest Rectangle in Histogram — *Stack*
Given an array representing histogram bar heights, find the area of the largest rectangle that can be formed within the histogram.

### 134. Median of Two Sorted Arrays — *Binary Search*
Given two sorted arrays, find the median of the combined dataset in O(log(m+n)).

### 135. Merge k Sorted Lists — *Linked List*
Given an array of `k` sorted linked lists, merge them into one sorted linked list.

### 136. Reverse Nodes in k-Group — *Linked List*
Given a linked list, reverse the nodes in groups of `k` and return the modified list (leave any remaining nodes fewer than `k` at the end untouched).

### 137. Binary Tree Maximum Path Sum — *Trees*
Given a binary tree, find the maximum sum of any path between any two nodes (the path doesn't need to pass through the root).

### 138. Word Search II — *Tries*
Given a 2D grid of letters and a list of words, find all words from the list that can be formed by tracing paths of adjacent cells.

### 139. Find Median from Data Stream — *Heap / Priority Queue*
Design a data structure that supports adding integers one at a time from a stream and returning the median of all numbers seen so far, at any point.

### 140. N-Queens — *Backtracking*
Given an integer `n`, place `n` queens on an n×n chessboard so no two queens attack each other (same row, column, or diagonal). Return all distinct solutions.

### 141. Word Ladder — *Graphs*
Given a start word, an end word, and a word list, find the length of the shortest transformation sequence where each step changes exactly one letter and the result must be a valid word in the list.

### 142. Reconstruct Itinerary — *Advanced Graphs*
Given a list of airline tickets (from-to pairs), reconstruct the itinerary in order, starting from "JFK", using all tickets exactly once, choosing the lexicographically smallest route when multiple valid ones exist.

### 143. Swim in Rising Water — *Advanced Graphs*
Given an n×n grid where each cell has an elevation, and water rises over time, find the minimum time needed to swim from the top-left to bottom-right (you can only move to a cell if the current water level is at or above its elevation).

### 144. Alien Dictionary — *Advanced Graphs*
Given a list of words from an alien language sorted according to that language's unknown alphabet order, determine a valid character order for that alphabet.

### 145. Longest Increasing Path in a Matrix — *2-D Dynamic Programming*
Given an m×n matrix, find the length of the longest path where each step moves to an adjacent cell with a strictly greater value.

### 146. Distinct Subsequences — *2-D Dynamic Programming*
Given two strings `s` and `t`, count the number of distinct ways `t` can appear as a subsequence of `s`.

### 147. Burst Balloons — *2-D Dynamic Programming*
Given an array representing balloons with numbers, bursting a balloon gives coins equal to the product of its neighbors' numbers (and adjacent boundaries). Find the maximum coins obtainable by bursting all balloons in some order.

### 148. Regular Expression Matching — *2-D Dynamic Programming*
Implement regular expression matching supporting `.` (matches any single character) and `*` (matches zero or more of the preceding element), determining if a pattern matches an entire string.

### 149. Minimum Interval to Include Each Query — *Intervals*
Given a list of intervals and a list of query points, for each query find the size of the smallest interval that contains it (or -1 if none does).

---

## How to Use This

- Read the description, code your solution directly in your editor/repo — no need to open LeetCode first.
- Once you believe it's correct, search the exact problem name on leetcode.com and paste your solution in to run it against their full test suite (these descriptions are simplified — LeetCode's official constraints/edge cases are more exhaustive).
- Easy tier → commit the finished solution same day.
- Medium/Hard tier → commit planning notes, brute-force attempts, and refactors as you go (per your `notes/` + `learnings.md` setup).

## Progress Log

| Date | # | Problem | Difficulty | Notes |
|------|---|---------|------------|-------|
| | | | | |
