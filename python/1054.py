class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        import heapq as hq
        from collections import Counter
        nums_with_count = [(-1*count, num) for num, count in Counter(barcodes).items()]
        hq.heapify(nums_with_count)
        ans = []
        while nums_with_count:
            cur_cnt, num = hq.heappop(nums_with_count)
            ans.append(num)
            if cur_cnt < -1:
                cur_cnt += 1
                nums_with_count.append((cur_cnt, num))
        return ans
