class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}

        for ch in s:

            # closing bracket
            if ch in pairs:
                # stack empty OR mismatch
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()

            # opening bracket
            else:
                stack.append(ch)

        return len(stack) == 0