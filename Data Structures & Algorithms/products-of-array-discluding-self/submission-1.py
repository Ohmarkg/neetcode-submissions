class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftProduct = nums[:]
        rightProduct = nums[:]
        
        #leftProduct
        product = 1
        for i in range(len(nums)):
            leftProduct[i] = product
            product *= nums[i]
        
        product = 1
        for i in range(len(nums) - 1 , -1 , -1):
            rightProduct[i] = product
            product *= nums[i]
        return [ rightProduct[i] * leftProduct[i] for i in range(len(nums))]    

       