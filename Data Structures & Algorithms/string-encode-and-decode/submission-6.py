class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            length = len(word)
            string += str(length) + "#" + word
        return string

    def decode(self, s: str) -> List[str]:

        i = 0
        final = []
        while i < len(s):

            #handle digit
            length = ""
            while s[i] != "#":
                length += s[i]
                i+=1
            length = int(length)
            i+=1
            final.append(s[i:i+length])
            i += length
        return final
