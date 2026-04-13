class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We can use prefix and suffix sum technique

        # 1. Compute the prefix product of every element 

        prefix_product = [0 for _ in range(len(nums))]
        prefix_product[0] = 1

        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

        # 2. Compute the sufix product of every element (same as prefix, but reversal)

        sufix_product = [0 for _ in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                sufix_product[i] = 1
            else:
                sufix_product[i] = sufix_product[i + 1] * nums[i + 1]
        
        # 3. Build the solution array, multiplying each prefix by sufix for each pos

        sol = []

        for i in range(len(nums)):
            sol.append(prefix_product[i] * sufix_product[i])
        
        return sol