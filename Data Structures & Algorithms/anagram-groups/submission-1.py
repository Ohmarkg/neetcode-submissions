class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #dictionary to track frequency 
        freq = defaultdict(list)
        for word in strs:

            count = [0] * 26
            for let in word:

                #adjust count and position
                count[ord(let) - ord('a')]+=1
            key = ",".join(map(str,count))
            freq[key].append(word)
        
        return list(freq.values())


        