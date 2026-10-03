class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        

        for i,word in enumerate(strs):
            counts = [0] * 26
            for let in word:
                counts[ord(let) % ord('a')] += 1
            key = tuple(counts)
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        finalList = []
        for key in anagrams:
            finalList.append(anagrams[key])
        return finalList