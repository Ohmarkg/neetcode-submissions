class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #list of list to hold it 
        buckets  = [[] for num in nums]
        sol = []
        freq = {}
        for num in nums:

            if num in freq:
                freq[num] += 1
            else:
                freq[num] =  1
        
        #add them to the buckets
        #acces num freq place in bucket[freq] = num

        for num in freq:
            buckets[freq[num] -1].append(num)
        for i in range(len(buckets) - 1, -1, -1 ):

            if buckets[i] == []:
                continue
            else:
                for num in buckets[i]:
                    sol.append(num)
        
        return sol[:k]