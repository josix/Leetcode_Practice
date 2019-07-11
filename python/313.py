class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq as hq
        seen = {1}
        ugly_heap = [1]
        ans = []
        while n > 0:
            ugly = hq.heappop(ugly_heap)
            ans.append(ugly)
            for num in [ n*ugly for n in primes]:
                if num not in seen:
                    hq.heappush(ugly_heap, num)
                    seen.add(num)
            n -= 1
        return ans[-1]
        
        
