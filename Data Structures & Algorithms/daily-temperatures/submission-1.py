class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        
        for i in range(len(temperatures)):
            cur_temp = temperatures[i]

            for j in range(i + 1, len(temperatures)):
                future_temp = temperatures[j]
                
                if future_temp > cur_temp:
                    result[i] = j - i
                    break
        
        return result
            