class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import bisect

        n = len(matrix[0]) - 1
        left = 0
        right = len(matrix) - 1

        while (left <= right):
            mid = (right - left // 2) + left
            last_el_row = matrix[mid][n]
            if last_el_row == target:
                return True
            
            if target > last_el_row:
                left = mid + 1
            else: 
                first_el_row = matrix[mid][0]
                if first_el_row == target:
                    return True
                
                if target < first_el_row:
                    right = mid - 1
                else:
                    break
        
        idx = bisect.bisect_left(matrix[mid], target)

        return True if idx <= n and matrix[mid][idx] == target else False 
        