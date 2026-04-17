class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        sol = set()

        for i in range(0, len(nums)):
            left = i + 1
            right = len(nums) - 1

            target = -nums[i]

            while left < right:
                sum_lr = nums[left] + nums[right]

                if sum_lr == target:
                    sol.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    continue

                if sum_lr < target:
                    left += 1
                    continue
                
                if sum_lr > target:
                    right -= 1
                    continue

        return [list(el) for el in sol]


        