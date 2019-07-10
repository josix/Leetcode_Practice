class Solution:
    def reorganizeString(self, S: str) -> str:
        from collections import Counter
        import heapq as hq
        char_count = [(-1*count,word) for word, count in Counter(S).items()]
        hq.heapify(char_count)
        ans = ""
        while char_count:
            current_count, next_char = hq.heappop(char_count)
            if ans != "" and ans[-1] == next_char:
                ans = ""
                break
            ans += next_char
            if -1*current_count > 1:
                current_count += 1
                char_count.append((current_count, next_char))
        return ans
        
