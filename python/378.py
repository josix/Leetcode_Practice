class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        all_nums = [ele for row in matrix for ele in row]
        import heapq as hq
        return hq.nsmallest(k, all_nums)[-1]
