class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # In the naive solution we can compare each string with every other string
        # and group they if are equals

        # A better approach we can sort every string and store in a array
        # We build a hash map with each sorted string, and a list of indexes
        # After this, we traverse the hashmap, building each list of anagrams

        # 1. Create a list of each string sorted
        sorted_strs = ["".join(sorted(s)) for s in strs] # O(mlogm * n) or O(n) since m is const (1000) 

        # 2. Create a hashmap of s -> [indexes], traversing each string in sorted_strs
        anagram_indexes = {}
        
        for idx, s in enumerate(sorted_strs): # O(n)
            if s in anagram_indexes:
                anagram_indexes[s].append(idx)
            else:
                anagram_indexes[s] = [idx] 

        # 3. Build the solution array, reconstructing the array of anagrams based on hashmap list of indexes
        sol = []

        for key, idx_list in anagram_indexes.items():
            anagram_list = [strs[idx] for idx in idx_list]
            sol.append(anagram_list)

        return sol 
        