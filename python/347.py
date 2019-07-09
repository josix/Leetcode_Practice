class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq as hq
        from collections import Counter
        num_to_count = Counter(nums)
        return hq.nlargest(k, num_to_count.keys(), key=num_to_count.get)
        
