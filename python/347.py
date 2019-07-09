class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq as hq
        num_to_count = {}
        for num in nums:
            if num not in num_to_count:
                num_to_count[num] = 1
            else:
                num_to_count[num] += 1
        nums_with_count = [(count, num) for num, count in num_to_count.items()]
        hq.heapify(nums_with_count)
        return [num for _, num in hq.nlargest(k, nums_with_count)]
        
