class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        maxSum = float("-inf")
        r = 0
        windowSum = 0
        while r < len(nums):
            windowSum+= nums[r]
            if r-l + 1 == k:
                maxSum = max(maxSum, windowSum)
                windowSum-=nums[l]
                l+=1
            r+=1
        return maxSum / k