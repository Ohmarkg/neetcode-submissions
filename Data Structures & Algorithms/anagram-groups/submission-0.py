class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for word in strs:
            temp = word[:]
            temp = "".join(sorted(word))
            if temp in anagrams:
                anagrams[temp].append(word)
            else:
                anagrams[temp] = []
                anagrams[temp].append(word)
        
        last = []
        for key in anagrams:
            last.append(anagrams[key])
        return last
        