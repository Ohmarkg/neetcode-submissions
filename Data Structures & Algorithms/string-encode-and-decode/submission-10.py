class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for word in strs:
            encodedString += f'{len(word)}@{word}'
        return encodedString

    def decode(self, s: str) -> List[str]:

        decoded = []
        i = 0
        print(s)
        while i < len(s):
            length = ""
            while s[i] != '@':
                length += s[i]
                i += 1
            length = int(length)
            decoded.append(s[i+1: i + length + 1])
            i += length + 1
        return decoded



