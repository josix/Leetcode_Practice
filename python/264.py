class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq as hq
        seen = {1}
        ugly_heap = [1]
        ans = []
        while n > 0:
            ugly = hq.heappop(ugly_heap)
            ans.append(ugly)
            for num in [ugly*2, ugly*3, ugly*5]:
                if num not in seen:
                    hq.heappush(ugly_heap, num)
                    seen.add(num)
            n -= 1
        return ans[-1]
