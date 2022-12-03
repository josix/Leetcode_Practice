class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        max_sub_length = 0
        current_substring = ""
        substring_length = len(current_substring)
        start_pos = 0
        end_pos = 0
        while end_pos != len(s): 								# O(N)
            candidate_substring = s[start_pos: end_pos]						# <= O(N)
            if s[end_pos] not  in set(current_substring):						# <= O(N)
                current_substring += s[end_pos]							# O(1)
            elif s[end_pos] in set(current_substring):						# <= O(N)
                current_substring = current_substring[current_substring.find(s[end_pos]) + 1:] + s[end_pos]
                print(current_substring)
    # O(m), where m is the length to the repetitive letter + O(1)
            substring_length = len(current_substring)				# < O(N)
            max_sub_length = max(max_sub_length, substring_length) 		# O(1)
            end_pos += 1								# O(1)
        return max_sub_length