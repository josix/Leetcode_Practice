# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        slow, fast = 0, len(s) - 1
        while slow < fast:
            while slow < fast and not s[slow].isalnum():
                slow += 1
            while slow < fast and not s[fast].isalnum():
                fast -= 1
            if s[slow].lower() != s[fast].lower():
                return False
            slow += 1
            fast -= 1
        return True
