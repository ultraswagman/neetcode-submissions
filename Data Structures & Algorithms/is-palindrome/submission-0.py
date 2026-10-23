class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = []
        comparator = []
        for char in s.lower():
            if char.isalnum():
                comparator.append(char)

        for char in s.lower()[::-1]:
            if char.isalnum():
                reverse.append(char)
        return reverse == comparator