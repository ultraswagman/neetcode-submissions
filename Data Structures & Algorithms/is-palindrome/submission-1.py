class Solution:
    def isPalindrome(self, s: str) -> bool:
        comparator = []
        for char in s.lower():
            if char.isalnum():
                comparator.append(char)

        reverse = comparator[::-1]
        return reverse == comparator