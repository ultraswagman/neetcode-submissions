class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_1 = {}
        seen_2 = {}
        for char in s:
            seen_1[char] = seen_1.get(char, 0) + 1
        for char in t:
            seen_2[char] = seen_2.get(char, 0) + 1
        return seen_1 == seen_2