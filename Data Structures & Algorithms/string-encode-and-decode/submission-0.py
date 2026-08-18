class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = []
        for i in strs:
            encode.append(str(len(i)))
            encode.append("#")
            encode.append(i)
        return "".join(encode)
    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            start = i
            while s[i] != '#':
                i += 1
            length = int(s[start:i])
            i +=1
            decoded.append(s[i:i+length])
            i += length
        return decoded
