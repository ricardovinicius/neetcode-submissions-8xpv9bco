class Solution:
    def verify(self, piles, h, k) -> int:
        for pile in piles:
            h -= math.ceil(pile / k)

        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        h_max = max(piles)

        left = 1
        right = h_max

        while (left < right):
            mid = ((right - left) // 2) + left

            v = self.verify(piles, h, mid)

            if (v < 0):
                left = mid + 1
            else:
                right = mid
        
        return right
