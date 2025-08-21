class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opposites = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in opposites:
                if stack and stack[-1] == opposites[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
