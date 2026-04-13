class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort solution
        # 1. Count the frequency of each element
        from collections import Counter

        freq_count = Counter(nums)
        
        # 2. Create a tuple list of (freq, element)
        freq_tuple_list = [(freq, element) for element, freq in freq_count.items()]

        # 3. Create buckets for each frequency 
        freq_buckets = [[] for _ in range(len(nums) + 1)]

        # 4. Fill frequency buckets with each corresponding element 
        for freq in freq_tuple_list:
            freq_buckets[freq[0]].append(freq[1])

        # 5. Iterate reversely through the freq_buckets until k was grouped
        sol = []

        for i in reversed(range(len(freq_buckets))):
            for el in freq_buckets[i]:
                sol.append(el)

                if len(sol) >= k:
                    return sol
        
        return sol

