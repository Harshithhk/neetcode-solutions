class Solution:
    def containsDuplicate(self, nums) -> bool:
        visitors = {}
        for num in nums:
            if num in visitors:
                return True
            else:
                visitors[num] = 1

        return False
