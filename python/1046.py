class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq as hq
        neg_stones = [-1*stone for stone in stones]
        hq.heapify(neg_stones)
        while len(neg_stones) > 1:
            x, y = hq.heappop(neg_stones), hq.heappop(neg_stones)
            print(x,y)
            if x == y:
                continue
            else:
                hq.heappush(neg_stones, -1*(abs(x - y)))
            print(neg_stones)
        return -1 * hq.heappop(neg_stones) if len(neg_stones) == 1 else 0
