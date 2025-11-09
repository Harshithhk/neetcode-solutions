class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        char_set = set()

        for r in range(len(s)):
            # While we have a duplicate, shrink window from left
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            # Add current character to set
            char_set.add(s[r])

            # Update max length
            max_len = max(max_len, r - l + 1)

        return max_len
