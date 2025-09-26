class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        sub_s = set()

        while r < len(s):

            while s[r] in sub_s:
                sub_s.remove(s[l])
                l += 1

            sub_s.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
