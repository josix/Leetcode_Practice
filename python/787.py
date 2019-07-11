class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        from collections import defaultdict
        import heapq as hq
        graph = defaultdict(dict)
        heap = [(0, src, 0)]
        for source, destinition, weight in flights:
            graph[source][destinition] = weight
        while heap:
            cost, city, stops = hq.heappop(heap)
            if city == dst:
                return cost
            if stops <= K:
                for neighbor in graph[city]:
                    weight = graph[city][neighbor]
                    hq.heappush(heap, (cost + weight, neighbor, stops + 1))
        return -1
                
