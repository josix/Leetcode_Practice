# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def get_longest_common_prefix(str1, str2):
            i = 0
            result = ""
            while len(str1) > i and len(str2) > i:
                if str1[i] == str2[i]:
                    result += str1[i]
                else:
                    break
                i += 1
            return result
        from functools import reduce
        ans = reduce(get_longest_common_prefix, strs)
        return ans
                
