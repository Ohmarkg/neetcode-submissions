class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequency = {}

        for n in nums:
            numFrequency[n] = numFrequency.get(n,0) + 1
        count = [[] for i in range(len(nums))]
        
        for num in numFrequency:
            count[numFrequency[num] - 1].append(num)
        
        mostFreqK = []
        for i in range(len(nums)-1,-1,-1):
            for n in count[i]:
                mostFreqK.append(n)
                if len(mostFreqK) == k:
                    return mostFreqK
    

       
