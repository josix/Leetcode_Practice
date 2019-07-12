class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        from collections import defaultdict
        import heapq as hq
        graph = defaultdict(dict)
        heap = [(0, K)]
        for u, v, w in times:
            graph[u][v] = w
        seen = {}
        while heap:
            time, node = hq.heappop(heap)
            if node in seen:
                continue
            else:
                seen[node] = time
            for neighbor in graph[node]:
                if neighbor not in seen:
                    hq.heappush(heap, (time + graph[node][neighbor], neighbor))
        if len(seen) != N:
            return -1
        else:
            return max(seen.values())
        
