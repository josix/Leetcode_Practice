class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        candidate = [(row[0], i, 0) for i, row in enumerate(matrix)]
        import heapq as hq
        count = 0
        while count < k - 1:
            _, row_index, col_index = hq.heappop(candidate)
            count += 1
            if col_index != n - 1:
                hq.heappush(candidate, (matrix[row_index][col_index+1], row_index, col_index + 1))
            
        return hq.heappop(candidate)[0]
