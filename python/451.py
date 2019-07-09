class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        import heapq as hq
        char_to_freq = Counter(s)
        ans = []
        for c in hq.nlargest(len(s), char_to_freq.keys(), char_to_freq.get):
            for _ in range(char_to_freq[c]):
                ans.append(c)
        return "".join(ans)
        
        
