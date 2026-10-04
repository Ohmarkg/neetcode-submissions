from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # find a way to group the anagrams together
        # Use a dictionary to store them 
        
        anagrams = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for let in word:
                counts[ord(let) % ord('a')] += 1
            anagrams[tuple(counts)].append(word)
        return list(anagrams.values())