class Solution:

    def encode(self, strs: List[str]) -> str:
        sender = ""
        for s in strs:
            sender += str(len(s)) + "#" + s
        return sender
            
    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            output.append(s[j+1: j + length + 1])
            i = j + 1 + length
        return output

            
            