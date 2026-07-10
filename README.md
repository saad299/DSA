# DSA — Daily Coding Log

A running log of daily practice problems, organized by difficulty. Each tier has **10 programming problems** (classic exercises) and **10 real-world scenario problems** (practical situations you'd actually hit as a full-stack dev).

Rule of thumb: work top to bottom. Don't skip ahead to Hard/Legendary until Beginner–Intermediate feel automatic — the point is pattern recognition, not ego.

---

## 📗 Beginner
*Syntax, basic math, printing, simple conditionals — no loops needed.*

### Programming
1. Hello World — Print "Hello, World!" to the console
2. Basic Addition — Add two numbers and print the result
3. Rectangle Area — Find the area of a rectangle given width and height
4. Temperature Conversion — Convert a temperature from Celsius to Fahrenheit
5. Even/Odd Check — Check if a number is even or odd
6. Max of Two Numbers — Find the largest of two numbers
7. Variable Swap — Swap two variables without a third variable
8. Circle Calculations — Calculate the area and circumference of a circle
9. Time Conversion — Convert minutes into hours and minutes (e.g. 130 → 2h 10m)
10. Leap Year Check — Check if a given year is a leap year

### Real-World Scenarios
11. Tax Calculator — Calculate the total bill after adding a fixed tax percentage
12. Daily Pay Calculator — Given an hourly wage and hours worked, calculate the daily pay
13. Voting Eligibility — Check if a user is old enough to vote (age >= 18)
14. Currency Converter — Convert a given price from USD to PKR using a fixed exchange rate
15. BMI Calculator — Calculate BMI given height and weight, and print the category
16. Password Validator — Check if a password meets a minimum length requirement
17. Discount Calculator — Calculate the discount price given original price and discount %
18. Phone Number Validator — Determine if a given number is a valid Pakistani mobile number length
19. Shopping Cart Total — Calculate the total cost of items in a simple shopping cart (fixed quantity)
20. Time of Day — Check if a given time (in 24hr format) falls in AM or PM

---

## 📘 Easy
*Loops — for, while, nested loops.*

### Programming
21. Number Sequence — Print numbers from 1 to N
22. Factorial — Find the factorial of a number
23. Digit Sum — Find the sum of digits of a number
24. Prime Check — Check if a number is prime
25. Fibonacci Series — Print the Fibonacci series up to N terms
26. Number Reversal — Reverse a number (e.g. 123 → 321)
27. Vowel Counter — Count the number of vowels in a sentence
28. Multiplication Table — Print a multiplication table for a given number
29. Palindrome Check — Check if a string is a palindrome
30. Star Pattern — Print a right-angled triangle pattern using stars

### Real-World Scenarios
31. Attendance Percentage — Calculate the total attendance percentage given days present and total days
32. Invoice Generator — Generate an invoice number sequence for N orders (e.g. INV-001, INV-002...)
33. Temperature Average — Given daily temperatures for a week, find the average temperature
34. Weekend Counter — Count how many days in a month fall on a weekend (basic loop, no date libraries)
35. Compound Interest — Calculate compound interest year by year using a loop
36. Pass Counter — Given a list of exam scores, count how many students passed (score >= 40)
37. Countdown Timer — Simulate a countdown timer from N seconds to 0
38. Calorie Tracker — Calculate total calories burned given daily workout minutes over a week
39. Receipt Printer — Print a simple receipt listing item number and running total as items are added
40. Rent Projection — Given monthly rent and a yearly increase %, print rent for each of the next 5 years

---

## 📙 Intermediate
*Arrays and objects — manipulation, iteration, transformation.*

### Programming
41. Min/Max Finder — Find the largest and smallest number in an array
   - *Hint: track two variables while looping once — don't sort just for this.*
42. Array Deduplication — Remove duplicate values from an array
   - *Hint: a `Set` (or an object used as a lookup table) tracks what you've already seen.*
43. Manual Sort — Sort an array of numbers without using built-in sort
   - *Hint: implement bubble sort or selection sort — nested loop, compare and swap adjacent pairs.*
44. Sum and Average — Find the sum and average of an array of numbers
   - *Hint: accumulate a running total in the loop, divide by `array.length` at the end.*
45. Array Merge — Merge two arrays and remove duplicates
   - *Hint: concatenate first, then run it through a `Set` to dedupe.*
46. Frequency Counter — Count the frequency of each element in an array
   - *Hint: use an object (or `Map`) where keys are elements and values are counts.*
47. Second Largest — Find the second largest number in an array
   - *Hint: track both the largest and second-largest in a single pass, updating both on each comparison.*
48. Array Flattening — Flatten a nested array (one level deep)
   - *Hint: loop through and use `concat` or spread `...` on each sub-array into a result array.*
49. Object Builder — Create an object from two arrays (keys and values)
   - *Hint: loop by index and assign `obj[keysArray[i]] = valuesArray[i]`.*
50. Array Intersection — Find the intersection of two arrays
   - *Hint: convert one array to a `Set`, then filter the other array by checking membership in that set.*

### Real-World Scenarios
51. Out-of-Stock Finder — Given an array of product objects (name, price, stock), find all out-of-stock items
   - *Hint: `filter()` where `stock === 0`.*
52. Adult User Filter — Given an array of user objects, filter users older than 18
   - *Hint: `filter()` on the `age` property with a comparison.*
53. Revenue Calculator — Calculate total revenue from an array of order objects (each with price and quantity)
   - *Hint: `reduce()`, accumulating `price * quantity` for each order.*
54. Highest Salary Finder — Given an array of employee objects, find the employee with the highest salary
   - *Hint: `reduce()` comparing the current max against each employee's salary.*
55. Student Grouper — Group an array of student objects by their grade (A, B, C)
   - *Hint: build an object where each grade is a key mapping to an array of matching students.*
56. Income/Expense Tracker — Given an array of transactions, calculate total income vs total expenses
   - *Hint: loop once, branch on a `type` field (e.g. "income"/"expense") and accumulate two totals.*
57. Task Completion — Given a list of tasks (with status: done/pending), calculate completion percentage
   - *Hint: count how many have `status === "done"`, divide by total length, multiply by 100.*
58. City Population Sorter — Given an array of cities with population, sort them by population descending
   - *Hint: `array.sort((a, b) => b.population - a.population)`.*
59. Tag Search — Given an array of blog posts (with tags), find all posts containing a specific tag
   - *Hint: `filter()` where `post.tags.includes(targetTag)`.*
60. Cart Total with Tax — Given a cart array of objects (item, price, qty), calculate the final total with tax
   - *Hint: `reduce()` to get subtotal first, then apply `subtotal * (1 + taxRate)` at the end.*

---

## 📕 Hard
*Pure algorithms and DSA — recursion, searching, sorting, basic data structures.*

### Programming
61. Binary Search — Implement binary search on a sorted array
   - *Hint: keep `low` and `high` pointers, compare the middle element to your target each time.*
   - *Hint: if target is smaller, discard the right half; if larger, discard the left half.*
   - *Hint: this only works on a sorted array — sort first if it isn't.*
62. Bubble/Selection Sort — Implement bubble sort / selection sort manually
   - *Hint: bubble sort repeatedly swaps adjacent out-of-order pairs across passes.*
   - *Hint: selection sort finds the minimum of the unsorted portion and swaps it to the front.*
   - *Hint: both are O(n²) — fine for learning, not for large datasets.*
63. Two Sum — Solve the Two Sum problem (find pair summing to target)
   - *Hint: brute force is a nested loop — O(n²), works but slow.*
   - *Hint: better: use a hash map to store numbers you've seen and their indices as you go.*
   - *Hint: for each number, check if `target - number` already exists in the map.*
64. Anagram Check — Check if two strings are anagrams of each other
   - *Hint: sort both strings alphabetically and compare — simplest approach.*
   - *Hint: alternative: count character frequency in both and compare the counts.*
   - *Hint: remember to handle case sensitivity and whitespace if relevant.*
65. Stack Implementation — Implement a basic Stack using an array (push, pop, peek)
   - *Hint: `push` = `array.push()`, `pop` = `array.pop()` — arrays already behave like a stack at the end.*
   - *Hint: `peek` just returns the last element without removing it.*
   - *Hint: wrap it in a class or object so the operations feel like a proper data structure.*
66. Queue Implementation — Implement a Queue using an array (enqueue, dequeue)
   - *Hint: `enqueue` adds to the back (`push`), `dequeue` removes from the front (`shift`).*
   - *Hint: `shift()` is O(n) — for large-scale use, a linked-list-backed queue is faster, but array is fine here.*
   - *Hint: track a `front` pointer instead of using `shift()` if you want to optimize later.*
67. Missing Number — Find the missing number in an array of 1 to N
   - *Hint: the expected sum of 1 to N has a formula: `n*(n+1)/2`.*
   - *Hint: subtract the actual array sum from the expected sum — the difference is your missing number.*
   - *Hint: alternative: XOR all numbers 1 to N with all array elements — leftover is the missing one.*
68. Recursive Functions — Implement recursive factorial and recursive Fibonacci
   - *Hint: factorial's base case is `n <= 1 return 1`, recursive case is `n * factorial(n-1)`.*
   - *Hint: Fibonacci's base cases are `fib(0)=0, fib(1)=1`, recursive case is `fib(n-1) + fib(n-2)`.*
   - *Hint: naive recursive Fibonacci is exponential time — notice how slow it gets past n=35 or so.*
69. Cycle Detection — Detect if a linked list has a cycle (conceptually or with objects)
   - *Hint: use two pointers moving at different speeds — "slow" and "fast" (Floyd's algorithm).*
   - *Hint: fast pointer moves two nodes per step, slow moves one — if they ever meet, there's a cycle.*
   - *Hint: if fast pointer reaches the end (null), there's no cycle.*
70. Maximum Subarray Sum — Find the maximum sum of a contiguous subarray (Kadane's Algorithm)
   - *Hint: track a running sum, reset it to 0 whenever it goes negative.*
   - *Hint: keep a separate variable for the best sum seen so far, updated every step.*
   - *Hint: single pass, O(n) — no need to check every possible subarray.*

### Real-World Scenarios
71. Rate Limiter — Design a rate limiter that allows N requests per user per minute
   - *Hint: store a timestamp array (or count) per user in an object/map.*
   - *Hint: on each request, discard timestamps older than 60 seconds, then check the remaining count against N.*
   - *Hint: this is the "sliding window" rate-limiting pattern — look it up if stuck.*
72. Booking Overlap Detector — Given a list of flight bookings (departure/arrival times), detect overlapping bookings
   - *Hint: sort bookings by departure time first — makes overlap detection linear instead of quadratic.*
   - *Hint: compare each booking's departure time against the previous booking's arrival time.*
   - *Hint: overlap exists if `current.departure < previous.arrival`.*
73. LRU Cache — Implement a basic LRU cache for storing recently viewed products
   - *Hint: a `Map` in JS preserves insertion order, which is perfect for this.*
   - *Hint: on access, delete and re-insert the key to push it to the "most recent" end.*
   - *Hint: when capacity is exceeded, remove the first key in the map (the least recently used).*
74. Task Scheduler — Given a set of dependencies between tasks, determine a valid execution order (topological sort concept)
   - *Hint: model tasks and dependencies as a graph — each task points to tasks that depend on it.*
   - *Hint: use DFS, adding a task to the result only after all its dependencies are processed.*
   - *Hint: if you detect a cycle in the graph, no valid order exists.*
75. Duplicate Transaction Detector — Design an algorithm to detect duplicate transactions in a payment log within a time window
   - *Hint: group transactions by a key (e.g. user + amount), then check timestamps within each group.*
   - *Hint: two transactions are "duplicate" if they match on key fields and their timestamps are within X seconds.*
   - *Hint: a sliding window over sorted-by-time transactions avoids comparing every pair.*
76. Nearest Warehouse Finder — Given delivery locations with coordinates, find the nearest warehouse to each (basic distance calc)
   - *Hint: use the Euclidean distance formula: `sqrt((x2-x1)² + (y2-y1)²)`.*
   - *Hint: for each delivery location, loop through all warehouses and track the minimum distance found.*
   - *Hint: for real-world lat/long, you'd use the Haversine formula instead — but Euclidean is fine for practice.*
77. Autocomplete System — Implement a search autocomplete suggestion system using a prefix match (Trie concept)
   - *Hint: a Trie node has children (a map of letter → next node) and an `isEndOfWord` flag.*
   - *Hint: insert words letter by letter, creating child nodes as needed.*
   - *Hint: to autocomplete, walk down the Trie following the prefix, then collect all words below that node.*
78. Busiest Time Window — Given server logs with timestamps, find the busiest 1-hour window
   - *Hint: sort logs by timestamp, then use a sliding window of exactly 1 hour.*
   - *Hint: as you slide the window forward, add new entries and remove ones that fall outside the hour.*
   - *Hint: track the maximum count of entries seen in any window.*
79. Meeting Room Scheduler — Design an algorithm to detect if a set of appointments can fit without conflicts, given a single meeting room
   - *Hint: sort appointments by start time.*
   - *Hint: walk through and check if each appointment's start time is >= the previous appointment's end time.*
   - *Hint: any violation means a conflict — the whole set can't fit in one room.*
80. Coupon Optimizer — Given a list of coupon codes with expiry, filter and apply the best valid discount for a cart
   - *Hint: first filter out expired coupons by comparing expiry date to today's date.*
   - *Hint: among valid coupons, some may have minimum cart value requirements — filter those too.*
   - *Hint: from what remains, pick the one giving the maximum discount (compare computed discount amounts, not just %).*

---

## 📓 Legendary
*Advanced DSA — trees, graphs, dynamic programming, optimization.*

### Programming
81. Binary Search Tree — Implement a Binary Search Tree with insert, search, and delete
   - *Hint: insert: compare with the current node, go left if smaller, right if larger, recurse.*
   - *Hint: search follows the same left/right logic until it finds the value or hits a null.*
   - *Hint: delete is the tricky part — handle three cases: no children, one child, and two children (find the in-order successor).*
82. Graph Traversal — Implement DFS and BFS traversal on a graph
   - *Hint: DFS uses a stack (or recursion) — go as deep as possible before backtracking.*
   - *Hint: BFS uses a queue — explore all neighbors at the current depth before going deeper.*
   - *Hint: keep a `visited` set in both to avoid infinite loops on cyclic graphs.*
83. Longest Common Subsequence — Solve the Longest Common Subsequence problem (DP)
   - *Hint: build a 2D table where `table[i][j]` represents the LCS length of the first i and j characters of each string.*
   - *Hint: if characters match, `table[i][j] = table[i-1][j-1] + 1`; if not, take the max of the cell above or to the left.*
   - *Hint: the answer is in the bottom-right cell of the table.*
84. 0/1 Knapsack — Solve the 0/1 Knapsack problem (DP)
   - *Hint: build a 2D table where rows are items and columns are capacities from 0 to max.*
   - *Hint: for each item, decide: skip it (`table[i-1][cap]`) or take it (`value + table[i-1][cap-weight]`) — pick the max.*
   - *Hint: "0/1" means each item can only be used once — that's why you reference the *previous* row.*
85. Dijkstra's Algorithm — Find the shortest path in a weighted graph (Dijkstra's Algorithm)
   - *Hint: use a priority queue (or just track minimum distances in an array if the graph is small).*
   - *Hint: always process the unvisited node with the smallest known distance next.*
   - *Hint: relax edges — if going through the current node gives a shorter path to a neighbor, update it.*
86. Trie Implementation — Implement a Trie (prefix tree) for word storage and lookup
   - *Hint: same node structure as problem 77 — children map + `isEndOfWord` flag.*
   - *Hint: `insert(word)` walks/creates nodes character by character.*
   - *Hint: `search(word)` walks the same path and checks `isEndOfWord`; `startsWith(prefix)` just checks the path exists.*
87. N-Queens — Solve the N-Queens problem using backtracking
   - *Hint: place queens row by row, trying each column in the current row.*
   - *Hint: before placing, check if the position is safe (no queen shares the column or diagonal).*
   - *Hint: if a row has no safe position, backtrack — remove the previous queen and try the next column.*
88. Directed Graph Cycle Detection — Detect a cycle in a directed graph
   - *Hint: use DFS with two tracking sets: "visited" (fully processed) and "in current recursion path".*
   - *Hint: if you reach a node that's already in the current recursion path, you've found a cycle.*
   - *Hint: remove the node from the "recursion path" set once you're done exploring its branches.*
89. Advanced Sorting — Implement merge sort and quicksort from scratch
   - *Hint: merge sort splits the array in half recursively, then merges two sorted halves back together.*
   - *Hint: quicksort picks a pivot, partitions elements smaller/larger around it, then recurses on both sides.*
   - *Hint: the "merge" step and the "partition" step are the parts people get wrong — write and test those in isolation first.*
90. Longest Increasing Subsequence — Solve the Longest Increasing Subsequence problem (DP)
   - *Hint: `dp[i]` represents the length of the longest increasing subsequence ending at index i.*
   - *Hint: for each i, check all previous j < i — if `array[j] < array[i]`, `dp[i] = max(dp[i], dp[j]+1)`.*
   - *Hint: this is O(n²); there's an O(n log n) version using binary search if you want the extra challenge.*

### Real-World Scenarios
91. Friend Recommendation — Design a friend-recommendation system using graph traversal (mutual connections)
   - *Hint: model users and friendships as an undirected graph.*
   - *Hint: for a given user, do a 2-hop BFS — friends of friends who aren't already direct friends are candidates.*
   - *Hint: rank candidates by how many mutual friends they share (count of shared paths).*
92. Rider Assignment — Design an algorithm to optimally assign delivery riders to orders minimizing total distance
   - *Hint: this is a variant of the "assignment problem" — think of it as a bipartite graph (riders vs orders).*
   - *Hint: a simple greedy approach: repeatedly assign the closest available rider to the closest unassigned order.*
   - *Hint: for a truly optimal solution look up the Hungarian Algorithm — but greedy is a reasonable starting point.*
93. Fraud Detection — Design a system to detect fraudulent transaction patterns using graph relationships between accounts
   - *Hint: model accounts as nodes and transactions as directed edges.*
   - *Hint: look for suspicious structures — cycles (money moving in a loop back to origin), or one account with unusually high in/out degree.*
   - *Hint: DFS/BFS can detect cycles; degree counting is just a frequency map of edges per node.*
94. Route Planner — Design an efficient route planner between multiple cities given a road network with distances
   - *Hint: model cities as nodes, roads as weighted edges.*
   - *Hint: Dijkstra's algorithm gives shortest path from one city to all others.*
   - *Hint: if you need shortest paths between *all* pairs of cities, look into Floyd-Warshall instead.*
95. Job Scheduler — Design a job scheduler that maximizes profit given jobs with deadlines and durations (DP + greedy)
   - *Hint: sort jobs by deadline first.*
   - *Hint: greedy version: for each job, place it in the latest available time slot before its deadline.*
   - *Hint: if profit varies per job and slots are limited, this becomes a weighted scheduling DP problem — track best profit achievable per time slot.*
96. Product Recommendation — Design a system to recommend products based on "customers who bought X also bought Y" (graph-based)
   - *Hint: model this as a bipartite graph — customers on one side, products on the other, edges are purchases.*
   - *Hint: to find "also bought," look at all customers who bought X, then find other products those same customers bought.*
   - *Hint: count frequency of co-purchased products across customers, rank by count.*
97. Server Capacity Planning — Design an algorithm to detect the minimum number of servers needed to handle overlapping traffic spikes
   - *Hint: this is the classic "minimum meeting rooms" problem in disguise — traffic spikes are like appointments.*
   - *Hint: separate start times and end times into two sorted arrays.*
   - *Hint: walk through chronologically — increment a counter on a start, decrement on an end; track the maximum counter value.*
98. Edit Distance — Design a version-control-like diff algorithm to find the minimum edits between two file versions (Edit Distance)
   - *Hint: this is the classic Levenshtein Distance / Edit Distance DP problem.*
   - *Hint: build a 2D table where `table[i][j]` is the min edits to convert the first i characters into the first j characters.*
   - *Hint: each cell considers insert, delete, or replace — take the minimum of the three plus 1 (or 0 if characters match).*
99. Social Network Path — Design a social network's "shortest connection path" feature (like LinkedIn's "2nd degree connection")
   - *Hint: model the network as an unweighted graph — BFS naturally finds shortest paths in unweighted graphs.*
   - *Hint: run BFS from the source user, tracking the "depth" (degree of connection) at which the target user is found.*
   - *Hint: stop early once you find the target — no need to traverse the whole graph.*
100. Budget Allocation — Design a resource allocation system that partitions a cloud budget across teams to maximize utility (DP optimization)
   - *Hint: this is structurally similar to the Knapsack problem — budget is your "capacity," teams are your "items."*
   - *Hint: build a table where rows are teams and columns are budget amounts, storing max utility achievable.*
   - *Hint: for each team, decide how much of the remaining budget to allocate by checking all possible allocation amounts, not just take/skip.*

---

## Progress Log

| Date | Problem # | Title | Notes |
|------|-----------|-------|-------|
| | | | |

*Add a row each time you solve one — keeps the streak visible and the practice honest.*
