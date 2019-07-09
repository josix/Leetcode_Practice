class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """         
        from collections import Counter, defaultdict
        import heapq as hq
        word_to_freq = Counter(words)
        freq_to_word_list = defaultdict(list)
        for word, freq in word_to_freq.items():
            freq_to_word_list[freq].append(word)
        candidate = [ -1*freq for freq, word_list in freq_to_word_list.items()]
        hq.heapify(candidate)
        ans = []
        while len(ans) != k:
            smallest = hq.heappop(candidate)
            if freq_to_word_list[-1*smallest] == 1:
                ans.append(freq_to_word_list[-1*smallest])
            else:
                freq_to_word_list[-1*smallest].sort(reverse=True)
                while freq_to_word_list[-1*smallest] != [] and len(ans) != k:
                    ans.append(freq_to_word_list[-1*smallest].pop())
        return ans
            

