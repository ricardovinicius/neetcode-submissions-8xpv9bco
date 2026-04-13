class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Naive solution:
        # Create an hashmap frequency count of each element
        # Sort each element by they frequency as tuple in a array
        # Get top k elements of frequency sorted array

        from collections import Counter 
        import heapq

        counts = Counter(nums)

        freq_tuples = [(v, key) for key, v in counts.items()]

        heapq.heapify(freq_tuples)

        for _ in range(len(freq_tuples) - k):
            heapq.heappop(freq_tuples)

        return [t[1] for t in freq_tuples]
        