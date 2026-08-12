class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        usedK = 0
        count = float("-inf")
        while r< len(nums):
            if nums[r] == 0:
                usedK+=1
            while usedK > k:
                if nums[l] == 0:
                    usedK-=1
                l+=1

            count = max(count,r-l+1)
            r+=1

        return count

