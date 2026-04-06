class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compl = {}

        for idx, num in enumerate(nums):
            compl[target - num] = idx

        for i in range(len(nums)):
            if nums[i] in compl and i != compl[nums[i]]:
                return [i, compl[nums[i]]]
         