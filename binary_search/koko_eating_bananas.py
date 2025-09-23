class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            hours_taken = sum(math.ceil(pile / mid) for pile in piles)

            print(f"mid = {mid}, hours_taken = {hours_taken}")

            if hours_taken <= h:  # can finish, try slower
                r = mid - 1
            else:  # too slow, need to eat faster
                l = mid + 1

        return l
