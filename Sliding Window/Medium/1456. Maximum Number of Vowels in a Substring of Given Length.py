class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxVow = float("-inf")
        window = 0
        while r < len(s):
            if s[r] in "aeiou":
                window+=1
            if r-l + 1 == k:
                maxVow = max(window, maxVow)
                if s[l] in "aeiou":
                    window-=1
                l+=1
            r+=1

        return maxVow