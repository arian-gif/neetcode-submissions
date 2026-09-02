class Solution:
    def isValid(self, s: str) -> bool:
        if not s :
            return False
        pairs = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        stack = []

        for l in s:
            if l in pairs:
                if not stack:
                    return False
                pair = stack.pop()
                if pairs[l] != pair:
                    return False
            else:
                stack.append(l)
        return len(stack)==0

        