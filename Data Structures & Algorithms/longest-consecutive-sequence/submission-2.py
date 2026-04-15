class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import Counter

        nums_set = set(nums)

        if len(nums_set) == 0:
            return 0
        
        longest_seq = 1

        for num in nums:
            if num - 1 not in nums_set:
                cur_len = 1

                while num + cur_len in nums_set:
                    cur_len += 1
                
                if cur_len > longest_seq:
                    longest_seq = cur_len
                
        return longest_seq
                

        

