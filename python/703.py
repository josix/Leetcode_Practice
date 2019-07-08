class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq as hq
        self.hq = hq
        hq.heapify(nums)
        self.heap = nums
        self.k = k
        while len(self.heap) > k:
            hq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            self.hq.heappush(self.heap, val)
        else:
            self.hq.heappushpop(self.heap, val)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
