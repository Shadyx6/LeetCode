class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def comp(s):
            stack = []
            for i in s:
                if i =="#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return stack
            
        return comp(s) == comp(t)