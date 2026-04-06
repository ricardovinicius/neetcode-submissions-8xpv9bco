class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = {}

        for i in nums:
            if i in c:
                return True
            else:
                c[i] = 1

        return False
