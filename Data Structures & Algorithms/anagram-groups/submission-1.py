class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Traverse the str list, counting frequency of each letter
        # building an 26 pos array [], and building a hashmap of frequency
        # of same char counting
        anagram_dict = {}

        for s in strs:
            # Count frequency of each letter
            letter_freq = [0 for _ in range(26)]

            for c in s:
                letter_idx = ord(c) - ord('a')
                letter_freq[letter_idx] += 1
            
            # Since arrays are hashable in Python, we can use them as key
            if tuple(letter_freq) in anagram_dict:
                anagram_dict[tuple(letter_freq)].append(s)
            else:
                anagram_dict[tuple(letter_freq)] = [s]

        # 2. Build the solution, grouping each array of dict in a single list
        sol = [l for l in anagram_dict.values()]

        return sol
        