class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostfreq= 0
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
            mostfreq = max(freq[num],mostfreq)
        sol = []
        while k > 0:
            for key in freq:
                if freq[key] == mostfreq:
                    sol.append(key)
                    k -= 1
                    if k == 0:
                        break
            mostfreq -= 1
            
        return sol