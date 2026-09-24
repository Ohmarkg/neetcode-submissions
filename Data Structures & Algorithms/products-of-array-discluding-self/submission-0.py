class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left= [1 for num in nums]
        right = [1 for num in nums]

        for i in range(1,len(nums)):
            print(nums[i-1] , left[i-1])
            left[i] = nums[i-1] * left[i-1]

        for i in range(len(nums)-2,-1,-1):
            right[i] = nums[i+1] * right[i+1]
        
        final = []
        print(left,right)
        for i in range(len(left)):
            final.append(left[i]*right[i])
        return final


        

        