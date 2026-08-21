class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []

        for l in s:
            if l in pairs:
                if len(stack)==0:
                    return False
                pair = stack.pop()
                if pair != pairs[l]:
                    return False
            else:
                stack.append(l)
        
        return len(stack)==0

        