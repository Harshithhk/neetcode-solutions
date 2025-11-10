# Sliding Window Framework

A comprehensive guide to mastering sliding window problems in Data Structures & Algorithms.

---

## Table of Contents

- [When to Use Sliding Window](#when-to-use-sliding-window)
- [Core Concepts](#core-concepts)
- [Standard Templates](#standard-templates)
- [Common Patterns](#common-patterns)
- [Problem-Solving Workflow](#problem-solving-workflow)
- [Common Mistakes](#common-mistakes)
- [Complexity Analysis](#complexity-analysis)

---

## When to Use Sliding Window

### Key Indicators

Look for these clues in the problem statement:

- ✅ **Contiguous** subarray/substring (not subsequence)
- ✅ **Optimization** keywords: longest, shortest, maximum, minimum
- ✅ **Constraint-based**: with some condition to satisfy
- ✅ **Linear structure**: arrays, strings (not trees/graphs)

### Example Problems

- "Find the longest substring without repeating characters"
- "Minimum window substring containing all characters"
- "Maximum sum subarray of size K"
- "Count subarrays with at most K distinct elements"

---

## Core Concepts

### Window Validity

The first and most important question:

> **What makes a window valid or invalid?**

| Problem Type        | Valid Condition           |
| ------------------- | ------------------------- |
| No duplicates       | All elements are unique   |
| Sum constraint      | Sum ≤ target              |
| K distinct elements | Number of distinct ≤ K    |
| Contains pattern    | All pattern chars present |

### Two Pointers Strategy

- **Right pointer (`r`)**: Expands the window by moving forward
- **Left pointer (`l`)**: Shrinks the window when invalid
- Both pointers move in the **same direction** (never backwards)

---

## Standard Templates

### Template 1: Maximum/Longest Problems

```python
def sliding_window_max(array):
    left = 0
    result = 0
    window_data = {}  # or set(), or simple variables

    for right in range(len(array)):
        # Step 1: Add array[right] to window
        # Update window_data with new element

        # Step 2: Shrink window while INVALID
        while window_is_invalid():
            # Remove array[left] from window_data
            left += 1

        # Step 3: Window is valid, update result
        result = max(result, right - left + 1)

    return result
```

**When to use:** Finding longest/maximum valid window

**Key point:** Update result AFTER ensuring window is valid

---

### Template 2: Minimum/Shortest Problems

```python
def sliding_window_min(array):
    left = 0
    result = float('inf')
    window_data = {}

    for right in range(len(array)):
        # Step 1: Add array[right] to window
        # Update window_data with new element

        # Step 2: Shrink window while VALID
        while window_is_valid():
            # Update result BEFORE shrinking
            result = min(result, right - left + 1)
            # Remove array[left] from window_data
            left += 1

    return result if result != float('inf') else 0
```

**When to use:** Finding shortest/minimum valid window

**Key point:** Update result BEFORE shrinking (while still valid)

---

### Template 3: Fixed-Size Window

```python
def fixed_window(array, k):
    result = 0
    window_sum = 0

    for right in range(len(array)):
        # Add to window
        window_sum += array[right]

        # Maintain fixed size
        if right >= k:
            window_sum -= array[right - k]

        # Update result when window reaches size k
        if right >= k - 1:
            result = max(result, window_sum)

    return result
```

**When to use:** Window size K is specified in problem

**Key point:** Simpler pattern, just maintain size

---

## Common Patterns

### Pattern 1: No Duplicate Characters

```python
def lengthOfLongestSubstring(s):
    left = 0
    max_len = 0
    char_set = set()

    for right in range(len(s)):
        # Shrink while duplicate exists
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
```

**Data structure:** Set (only need presence)

**Invalid when:** Element already in set

---

### Pattern 2: At Most K Distinct Elements

```python
def at_most_k_distinct(s, k):
    left = 0
    result = 0
    char_count = {}

    for right in range(len(s)):
        # Add character
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        # Shrink while too many distinct
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        result = max(result, right - left + 1)

    return result
```

**Data structure:** HashMap (need frequency)

**Invalid when:** len(hashmap) > k

**Trick for "Exactly K":** `exactly_k(K) = at_most_k(K) - at_most_k(K-1)`

---

### Pattern 3: Sum/Product Constraint

```python
def max_subarray_sum_at_most_k(nums, k):
    left = 0
    result = 0
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        # Shrink while sum exceeds k
        while current_sum > k:
            current_sum -= nums[left]
            left += 1

        result = max(result, right - left + 1)

    return result
```

**Data structure:** Simple variable

**Invalid when:** sum > target (or other constraint)

---

### Pattern 4: Minimum Window Containing Pattern

```python
def min_window_substring(s, t):
    if not t or not s:
        return ""

    target_count = {}
    for char in t:
        target_count[char] = target_count.get(char, 0) + 1

    left = 0
    min_len = float('inf')
    min_start = 0
    required = len(target_count)
    formed = 0
    window_count = {}

    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        if char in target_count and window_count[char] == target_count[char]:
            formed += 1

        # Shrink while valid
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left

            window_count[s[left]] -= 1
            if s[left] in target_count and window_count[s[left]] < target_count[s[left]]:
                formed -= 1
            left += 1

    return "" if min_len == float('inf') else s[min_start:min_start + min_len]
```

**Data structure:** Two HashMaps

**Valid when:** All pattern characters present with correct frequency

---

## Problem-Solving Workflow

### Step 1: Understand the Problem (5 minutes)

```
Ask yourself:
□ What makes a window valid/invalid?
□ Am I finding maximum or minimum?
□ Is window size fixed or variable?
□ What constraint must be satisfied?
```

### Step 2: Choose Data Structure

```
Decision tree:
• Need frequency count? → HashMap/Dictionary
• Just presence/absence? → Set
• Simple sum/count? → Integer variable
• Need order? → Deque
```

### Step 3: Write Template Structure

```python
# Write this FIRST before filling in details:
left = 0
result = 0  # or float('inf') for minimum
data_structure = {}

for right in range(len(array)):
    # Add to window

    # Shrink if invalid
    while (condition):
        # Remove from window
        left += 1

    # Update result

return result
```

### Step 4: Trace Through Example

```
Pick a small example and trace by hand:
- What's in the window at each step?
- When does it become invalid?
- When do you update the result?
```

### Step 5: Code and Test

```
Test cases:
□ Empty input: []
□ Single element: [1]
□ All same: [5, 5, 5, 5]
□ All different: [1, 2, 3, 4]
□ Given examples
```

---

## Common Mistakes

### ❌ Mistake 1: Managing Both Pointers Manually

```python
# Wrong
while right < len(array):
    # ... logic ...
    right += 1  # Easy to forget!
```

```python
# Right
for right in range(len(array)):
    # ... logic ...
    # right auto-increments
```

### ❌ Mistake 2: Calculating Result Only at End

```python
# Wrong - might miss maximum in the middle
for right in range(len(array)):
    # ... expand window ...

return len(window)  # Only checks final window
```

```python
# Right - track maximum throughout
for right in range(len(array)):
    # ... expand window ...
    result = max(result, right - left + 1)

return result
```

### ❌ Mistake 3: Forgetting to Update Window Data

```python
# Wrong
while window_is_invalid():
    left += 1  # Moved pointer but didn't update data structure!
```

```python
# Right
while window_is_invalid():
    # Remove from data structure
    window_data.remove(array[left])
    left += 1
```

### ❌ Mistake 4: Wrong Initialization

```python
# Wrong for minimum problems
result = 0  # Will never find minimum!

# Right for minimum problems
result = float('inf')
```

### ❌ Mistake 5: Off-by-One in Window Size

```python
# Wrong
window_size = right - left  # Missing the +1

# Right
window_size = right - left + 1  # Inclusive of both ends
```

---

## Complexity Analysis

### Time Complexity

**O(n)** for most sliding window problems

**Why?** Each element is visited at most twice:

- Once by the right pointer (expanding)
- Once by the left pointer (shrinking)

Total operations: 2n = O(n)

### Space Complexity

**O(k)** where k depends on the window data structure

| Data Structure  | Space                        |
| --------------- | ---------------------------- |
| Set             | O(min(n, charset_size))      |
| HashMap         | O(min(n, distinct_elements)) |
| Fixed variables | O(1)                         |
| Deque           | O(window_size)               |

---

## Quick Reference Checklist

### Before Coding

- [ ] Identified window validity condition
- [ ] Chose appropriate data structure
- [ ] Determined if finding max or min
- [ ] Decided on initial result value (0 or infinity)

### While Coding

- [ ] Using `for` loop for right pointer
- [ ] Using `while` loop for left pointer shrinking
- [ ] Updating data structure when adding elements
- [ ] Updating data structure when removing elements
- [ ] Updating result at correct time

### After Coding

- [ ] Tested with empty input
- [ ] Tested with single element
- [ ] Tested with all same elements
- [ ] Tested with all different elements
- [ ] Traced through example by hand

---

## Practice Problems by Difficulty

### Easy

- Maximum Average Subarray I
- Contains Duplicate II
- Maximum Number of Vowels in Substring

### Medium

- Longest Substring Without Repeating Characters ⭐
- Longest Repeating Character Replacement
- Permutation in String
- Fruit Into Baskets
- Max Consecutive Ones III

### Hard

- Minimum Window Substring ⭐
- Sliding Window Maximum
- Substring with Concatenation of All Words

---

## Additional Tips

1. **Start simple**: Master fixed-size windows before variable ones
2. **Visualize**: Draw the window moving across array on paper
3. **Pattern recognition**: After 10-15 problems, patterns become clear
4. **Template first**: Always write template structure before details
5. **Debug systematically**: Print window state at each step if stuck

---

## Resources

- [NeetCode Sliding Window Playlist](https://neetcode.io)
- [LeetCode Sliding Window Problems](https://leetcode.com/tag/sliding-window/)

---

**Happy Coding! 🚀**

Remember: The key to mastering sliding window is recognizing when a window becomes invalid and knowing how to fix it.
