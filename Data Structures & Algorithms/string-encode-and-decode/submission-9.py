class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedString = ""
        for word in strs:
            encodedString += str(len(word)) + "@"+ word
        #5@fiver2@ba
        return encodedString

    def decode(self, s: str) -> List[str]:

        i = 0
        decoded = []
        while i < len(s):
            readNum = ""
            while s[i] != "@":
                readNum += s[i]
                i += 1
            num =  int(readNum)
            decoded.append(s[i + 1 : i + num + 1])
            i += num + 1
        return decoded

