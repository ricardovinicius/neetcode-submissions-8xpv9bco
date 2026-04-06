class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_1 = {}
        c_2 = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in c_1:
                c_1[i] += 1
            else:
                c_1[i] = 1
        
        for i in t:
            if i in c_2:
                c_2[i] += 1
            else:
                c_2[i] = 1

        for i in c_1:
            if i in c_2:
                if c_1[i] != c_2[i]:
                    return False
            else:
                return False

        return True