class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def count_smaller(mid):
            smaller_num = 0
            i, j = len(matrix) - 1, 0
            while i >= 0 and j <= len(matrix) - 1:
                if matrix[i][j] <= mid:
                    smaller_num += i + 1
                    j += 1
                else:
                    i -= 1
            return smaller_num
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            count = count_smaller(mid)
            if count < k:
                left = mid + 1 # plus one is important
            else:
                right = mid
        return left
            
