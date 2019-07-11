class Solution:
    def isUgly(self, num: int) -> bool:
        def ugly(n):
            if n == 0:
                return False
            elif n % 2 == 0:
                return ugly(n/2)
            elif n % 3 == 0:
                return ugly(n/3)
            elif n % 5 == 0:
                return ugly(n/5)
            elif n == 1:
                return True
            else:
                return False
        return ugly(num)
            
        
