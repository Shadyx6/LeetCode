class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        maxLen = float("inf")
        maxSum = 0
        while r < len(nums):
            maxSum+= nums[r]
            while maxSum >=target:
                maxLen = min(maxLen, r - l + 1)
                maxSum-=nums[l]
                l+=1
            r+=1

        if maxLen == float("inf"):
            return 0
        return maxLen
        