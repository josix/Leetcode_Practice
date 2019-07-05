class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        product_at_k = 1
        for i in nums:
            ans += [product_at_k]
            product_at_k *= i
        
        product_at_k = 1
        length = len(nums)
        for i, num in enumerate(nums[::-1]):
            ans[length - i - 1] *= product_at_k
            product_at_k *= num
        return ans
        
