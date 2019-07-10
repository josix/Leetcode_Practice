class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq as hq
        if nums1 == [] or nums2 == [] or k == 0:
            return []
        heap = [(nums1[0] + nums2[0], 0, 0)]
        seen = set((0, 0))
        ans = []
        while len(ans) < k and heap:
            _ , pos_1, pos_2 = hq.heappop(heap)
            ans.append([nums1[pos_1], nums2[pos_2]])
            if pos_1 != len(nums1) - 1 and (pos_1 + 1, pos_2) not in seen:
                hq.heappush(heap, (nums1[pos_1 + 1]+nums2[pos_2], pos_1 + 1, pos_2))
                seen.add((pos_1 + 1, pos_2))
            if pos_2 != len(nums2) - 1 and (pos_1, pos_2 + 1) not in seen:
                hq.heappush(heap, (nums1[pos_1] + nums2[pos_2 + 1], pos_1, pos_2 + 1))
                seen.add((pos_1, pos_2 + 1))
        return ans
            
