class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        for num in nums: 					# O(N)
            heapq.heappush(hq, -num) 			# O(logN)
        for _ in range(k - 1):				# O(k)
            heapq.heappop(hq)				# O(logN)
        return -heapq.heappop(hq)				# O(logN)

        
