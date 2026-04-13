class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Naive solution:
        # Create an hashmap frequency count of each element
        # Sort each element by they frequency as tuple in a array
        # Get top k elements of frequency sorted array

        from collections import Counter

        counts = Counter(nums)

        freq_tuples = [(v, key) for key, v in counts.items()]

        sorted_freq_tuples = sorted(freq_tuples, reverse=True)

        return [t[1] for t in sorted_freq_tuples[:k]]
        