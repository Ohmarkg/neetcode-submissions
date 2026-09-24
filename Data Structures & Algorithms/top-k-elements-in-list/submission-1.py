class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #structure to store numbers at each index
        counts = [[] for i in range(len(nums) + 1)]
        #count the occurence of each numm
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        for num,occ in freq.items():
            counts[occ].append(num)
        
        last = []
        for i in range(len(counts)-1,-1,-1):
            for num in counts[i]:
                if k == 0:
                    break
                last.append(num)
                k -= 1  
            if k == 0:
                break
        return last

            