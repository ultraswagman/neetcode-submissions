class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for p in s:
            if p in "([{":
                stack.append(p)
            else:
                if not stack:
                    return False
                if stack[-1] != pairs[p]:
                    return False
                stack.pop()
        return not stack